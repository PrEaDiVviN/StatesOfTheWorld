import copy
from Services.ScrapperService.Scrapper import Scrapper
from Services.RequestService.HttpRequestService import HttpRequestService


class TaraDataObtainer:
    """ A wrapping class used to obtain all the countries Tara entity data. """
    def __init__(self):
        """Initializes TaraDataObtainer with the href of the link to scrap from."""
        self.html_text = ""
        self.href_wiki_states = "https://ro.wikipedia.org/wiki/Lista_statelor_lumii"

    def get_html_text(self):
        """ A function which wraps HttpRequestService.get_html_from_request and sets to variable html_text its result. """
        self.html_text = HttpRequestService.get_html_from_request(self.href_wiki_states)

    def get_tara_data(self):
        """ A function that gets all countries Tara entity data and return it as a list of lists where each list
        contains an entity with elements in the following order: tara_nume_scurt, tara_nume_oficial_corect, tara_link,
        capitala_nume, capitala_link.
        :return: A list of Tara entities
        """
        tari_list = list()
        tbody = Scrapper.find_first(self.html_text, "tbody")
        list_tr = Scrapper.find_all(tbody, "tr")
        for i in range(1, len(list_tr)):
            list_td = Scrapper.find_all(list_tr[i], "td")
            b_tara = Scrapper.find_first(list_td[0], "b")
            a_tara = Scrapper.find_first(b_tara, "a")
            tara_link = Scrapper.get_attribute_value(a_tara, "href")
            tara_nume_scurt = Scrapper.get_inner_text(a_tara)
            list_span = Scrapper.find_all(list_td[0], "span")
            tara_nume_oficial = list()
            if len(list_span) == 2:
                tara_nume_oficial.append(Scrapper.get_inner_text(list_span[1]))
            else:
                td_inner_text = Scrapper.get_inner_text(list_td[0])
                td_removed_b = Scrapper.remove_element_from_html(td_inner_text, "b")
                line_delimited_text = Scrapper.get_substring_from_item(td_removed_b, "-")
                if line_delimited_text != "":
                    tara_nume_oficial.append(copy.deepcopy(line_delimited_text[2:]))
                divide_delimited_text = Scrapper.get_substring_from_item(td_removed_b, ":")
                if divide_delimited_text != "":
                    tara_nume_oficial.append(copy.deepcopy(divide_delimited_text[2:]))
            capitala_nume = list()
            capitala_link = list()
            if "capitala" in list_td[4].lower() or "capitală" in list_td[4].lower():
                capitala_html = Scrapper.get_substring_from_item(list_td[4], "Capital")
                a_capitala = Scrapper.find_first(capitala_html, "a")
                capitala_nume.append(Scrapper.get_inner_text(a_capitala))
                capitala_link.append(Scrapper.get_attribute_value(a_capitala, "href"))
            else:
                if "capitale" in list_td[4].lower():
                    capitale_html = Scrapper.get_substring_from_item(list_td[4], "Capitale")
                    capitale_html_until_p = Scrapper.get_substring_from_item_till_end(capitale_html, "</p>")
                    a_capitale = Scrapper.find_all(capitale_html_until_p, "a")
                    capitala_nume.append("")
                    capitala_link.append("")
                    for a_capitala in a_capitale:
                        if capitala_nume[0] == "":
                            capitala_nume[0] = capitala_nume[0] + Scrapper.get_inner_text(a_capitala)
                            capitala_link[0] = capitala_link[0] + Scrapper.get_attribute_value(a_capitala, "href")
                        else:
                            capitala_nume[0] = capitala_nume[0] + ", " + Scrapper.get_inner_text(a_capitala)
                            capitala_link[0] = capitala_link[0] + ", " + Scrapper.get_attribute_value(a_capitala, "href")

            tara_nume_oficial_corect = tara_nume_oficial[0].removesuffix("\n")
            if len(capitala_nume) == 0:
                capitala_nume.append("")
            if len(capitala_link) == 0:
                capitala_link.append("")
            tari_list.append((tara_nume_scurt, tara_nume_oficial_corect, tara_link, capitala_nume[0], capitala_link[0]))
        return tari_list


if __name__ == "__main__":
    obtain = TaraDataObtainer()
    obtain.get_html_text()
    countries = obtain.get_tara_data()
    for country in countries:
        print(country)
