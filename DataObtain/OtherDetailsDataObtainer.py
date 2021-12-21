import copy
import re

from Services.ScrapperService.Scrapper import Scrapper
from Services.RequestService.HttpRequestService import HttpRequestService


class OtherDetailsDataObtainer:
    html_text = ""
    href_wiki_domain = "https://ro.wikipedia.org"

    def get_html_text(self, route):
        self.html_text = HttpRequestService.get_html_from_request(self.href_wiki_domain + route)

    def get_tara_steaguri_data(self):
        tbody = Scrapper.find_first_with_attribute(self.html_text, "table", 0, 'class="infocaseta"')
        tr_list = Scrapper.find_all(tbody, "tr")
        inner_table = Scrapper.get_substring_from_item(tr_list[2], "table")
        tr = Scrapper.find_first(inner_table, "tr")
        a_list = Scrapper.find_all(inner_table, "a")
        drapel_link = Scrapper.get_attribute_value(a_list[0], "href")
        stema_link = Scrapper.get_attribute_value(a_list[1], "href")
        tara_steaguri = list()
        tara_steaguri.append(drapel_link)
        tara_steaguri.append(stema_link)
        return tara_steaguri

    def get_geografie_data(self):
        html_text_removed_trouble_table = Scrapper.remove_element_from_html_with_attribute(self.html_text, "table", 0, 'align')
        html_text_removed_trouble_table_2 = Scrapper.remove_exact_element(html_text_removed_trouble_table, "table", 0)
        html_text_removed_trouble_table_3 = Scrapper.remove_exact_element(html_text_removed_trouble_table_2, "table", 0)
        html_text_removed_trouble_table_4 = Scrapper.remove_exact_element(html_text_removed_trouble_table_3, "table", 0)

        table = Scrapper.find_first_with_attribute(html_text_removed_trouble_table_4, "table", 0, 'class="infocaseta"')
        tbody = Scrapper.get_inner_text(table)
        tr_list = Scrapper.find_all(tbody, "tr")

        suprafata_totala = ""
        procent_apa = ""
        cel_mai_inalt_punct_nume = ""
        cel_mai_inalt_punct_link = ""
        cel_mai_inalt_punct_inaltime = ""
        cel_mai_jos_punct_nume = ""
        cel_mai_jos_punct_link = ""
        cel_mai_jos_punct_inaltime = ""
        fus_orar = ""

        for tr in tr_list:
            if "total" in tr.lower() and suprafata_totala == "":
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                td_text_removed_sup = Scrapper.remove_exact_element(td_text, "sup")
                suprafata = Scrapper.get_substring_from_item_till_end(td_text_removed_sup, "(")
                suprafata_totala = suprafata_totala + suprafata.replace(" ", "").replace("&#160;", "").replace("&#32", "").replace(";", "").split("km")[0].split("<")[0]
                suprafata_totala = suprafata_totala.replace(",", "")
                suprafata_totala = suprafata_totala.replace(".","")
            elif "Apă" in tr:
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                el = td_text.rfind(">")
                td_text = td_text[el+1:]
                procent_apa = procent_apa + td_text.replace(" ", "").replace("&#160;", "").replace("&#32;", "")
            elif "Cel mai înalt punct" in tr:
                a = Scrapper.find_first(tr, "a")
                cel_mai_inalt_punct_link = cel_mai_inalt_punct_link + Scrapper.get_attribute_value(a, "href")
                cel_mai_inalt_punct_nume = cel_mai_inalt_punct_nume + Scrapper.get_inner_text(a)
                if "span" in cel_mai_inalt_punct_nume:
                    cel_mai_inalt_punct_nume = Scrapper.get_inner_text(cel_mai_inalt_punct_nume)
                result = re.search("\(\d+\.*\d*", tr)
                if result:
                    cel_mai_inalt_punct_inaltime = cel_mai_inalt_punct_inaltime + result.group(0).replace("(", "").replace(".", "")
            elif "Cel mai jos punct" in tr:
                a = Scrapper.find_first(tr, "a")
                cel_mai_jos_punct_link = cel_mai_jos_punct_link + Scrapper.get_attribute_value(a, "href")
                cel_mai_jos_punct_nume = cel_mai_jos_punct_nume + Scrapper.get_inner_text(a)
                if "span" in cel_mai_jos_punct_nume:
                    cel_mai_jos_punct_nume = Scrapper.get_inner_text(cel_mai_jos_punct_nume)
                result = re.search("\(\d+\.*\d*", tr)
                if result:
                    cel_mai_jos_punct_inaltime = cel_mai_jos_punct_inaltime + result.group(0).replace("(", "").replace(".", "")
            elif "Fus orar" in tr:
                td = Scrapper.find_first(tr, "td")
                parantesis = Scrapper.get_text_between_separators(td, "(", ")")
                a = Scrapper.find_first(td, "a")
                if parantesis != "":
                    a = Scrapper.find_first(parantesis, "a")
                fus_orar = fus_orar + Scrapper.get_inner_text(a)
                if "+" not in fus_orar:
                    td_text = Scrapper.get_inner_text(td)
                    plus = td_text.find("+")
                    fus_orar = fus_orar + td_text[plus:].replace(" ", "").replace(">","").replace(")","").replace("<","").split("/")[0]
        result = list()
        result.append(suprafata_totala)
        result.append(procent_apa)
        result.append(cel_mai_inalt_punct_nume)
        result.append(cel_mai_inalt_punct_link)
        result.append(cel_mai_inalt_punct_inaltime)
        result.append(cel_mai_jos_punct_nume)
        result.append(cel_mai_jos_punct_link)
        result.append(cel_mai_jos_punct_inaltime)
        result.append(fus_orar)
        return result


if __name__ == "__main__":
    obtain = OtherDetailsDataObtainer()
    obtain.get_html_text("/wiki/Tunisia")
    countries_flag = obtain.get_geografie_data()
    print(countries_flag)
    for country in countries_flag:
        print(country)
