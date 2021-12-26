import copy
import re
from Services.ScrapperService.Scrapper import Scrapper
from Services.RequestService.HttpRequestService import HttpRequestService


class OtherDetailsDataObtainer:
    def __init__(self):
        self.html_text = ""
        self.href_wiki_domain = "https://ro.wikipedia.org"

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

    def get_geografie_vecini_data(self):
        html_text_removed_trouble_table = Scrapper.remove_element_from_html_with_attribute(self.html_text, "table", 0, 'align')
        html_text_removed_trouble_table_2 = Scrapper.remove_exact_element(html_text_removed_trouble_table, "table", 0)
        html_text_removed_trouble_table_3 = Scrapper.remove_exact_element(html_text_removed_trouble_table_2, "table", 0)
        html_text_removed_trouble_table_4 = Scrapper.remove_exact_element(html_text_removed_trouble_table_3, "table", 0)

        table = Scrapper.find_first_with_attribute(html_text_removed_trouble_table_4, "table", 0, 'class="infocaseta"')
        tbody = Scrapper.get_inner_text(table)
        tr_list = Scrapper.find_all(tbody, "tr")

        lista_vecini = list()

        for tr in tr_list:
            if "Vecini" in tr:
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                td_without_sup = Scrapper.remove_element_from_html(td_text, "sup")
                while "<sup" in td_without_sup:
                    td_without_sup = Scrapper.remove_element_from_html(td_without_sup, "sup")
                a_list = Scrapper.find_all(td_without_sup, "a")
                for a in a_list:
                    vecin = copy.deepcopy(Scrapper.get_inner_text(a))
                    if "<img" not in vecin:
                        lista_vecini.append(vecin)
                break
        return list(dict.fromkeys(lista_vecini))

    def get_populatie_data(self):
        html_text_removed_trouble_table = Scrapper.remove_element_from_html_with_attribute(self.html_text, "table", 0, 'align')
        html_text_removed_trouble_table_2 = Scrapper.remove_exact_element(html_text_removed_trouble_table, "table", 0)
        html_text_removed_trouble_table_3 = Scrapper.remove_exact_element(html_text_removed_trouble_table_2, "table", 0)
        html_text_removed_trouble_table_4 = Scrapper.remove_exact_element(html_text_removed_trouble_table_3, "table", 0)

        table = Scrapper.find_first_with_attribute(html_text_removed_trouble_table_4, "table", 0, 'class="infocaseta"')
        tbody = Scrapper.get_inner_text(table)
        tr_list = Scrapper.find_all(tbody, "tr")

        populatie = ""
        populatie1 = ""
        densitate = ""

        for tr in tr_list:
            if "Recensământ" in tr and populatie == "":
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                td_without_sup = Scrapper.remove_element_from_html(td_text, "sup")
                while "<sup" in td_without_sup:
                    td_without_sup = Scrapper.remove_element_from_html(td_without_sup, "sup")
                populatie = populatie + (((td_without_sup.replace(",","")).replace(".","")).replace("$","").split("&")[0].split(";")[0]).replace(">","")
                populatie = populatie.replace("locuitor", "").replace("milioane", "").replace(">","").split("<")[0]
            elif "Densitate" in tr and densitate == "":
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                td_without_sup = Scrapper.remove_element_from_html(td_text, "sup")
                while "<sup" in td_without_sup:
                    td_without_sup = Scrapper.remove_element_from_html(td_without_sup, "sup")
                densitate = ((td_without_sup.replace("$", "")).replace(".", "")).split(",")[0].split("&")[0].split(";")[0].split("/")[0].replace(">","").replace("locuitor","").replace("loc","")
                densitate = densitate.replace(" (<a href=\"", "").replace("(2020) - ","").replace(">", "").replace("2011 (estimativ)","").replace(" ","")
        for tr in tr_list:
            if "Estimare" in tr:
                populatie1 = ""
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                td_without_sup = Scrapper.remove_element_from_html(td_text, "sup")
                while "<sup" in td_without_sup:
                    td_without_sup = Scrapper.remove_element_from_html(td_without_sup, "sup")
                populatie1 = populatie1 + ((td_without_sup.replace(",", "")).replace(".", "")).replace("$", "").split("(")[0].replace(" ","").split("&")[0].split(";")[0].replace(">","")
                populatie1 = populatie1.replace("locuitor","").replace("milioane", "").replace(">","").split("<")[0]
        if len(populatie1) > len(populatie):
            populatie = populatie1
        if len(populatie1) == len(populatie) and populatie1 > populatie:
            populatie = populatie1
        populatie = populatie.split("-")[0]
        if populatie.startswith(">") or populatie.startswith("<"):
            populatie = ""

        return [populatie, densitate]

    def get_limba_data(self):
        html_text_removed_trouble_table = Scrapper.remove_element_from_html_with_attribute(self.html_text, "table", 0, 'align')
        html_text_removed_trouble_table_2 = Scrapper.remove_exact_element(html_text_removed_trouble_table, "table", 0)
        html_text_removed_trouble_table_3 = Scrapper.remove_exact_element(html_text_removed_trouble_table_2, "table", 0)
        html_text_removed_trouble_table_4 = Scrapper.remove_exact_element(html_text_removed_trouble_table_3, "table", 0)

        table = Scrapper.find_first_with_attribute(html_text_removed_trouble_table_4, "table", 0, 'class="infocaseta"')
        tbody = Scrapper.get_inner_text(table)
        tr_list = Scrapper.find_all(tbody, "tr")

        limba_oficiala = ""
        link_limba_oficiala = ""
        etnonime = ""
        limbi_regionale_minoritate = ""

        for tr in tr_list:
            if "Limbi oficiale" in tr:
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                td_without_sup = Scrapper.remove_element_from_html2(td_text, "sup")
                while "<sup" in td_without_sup:
                    td_without_sup = Scrapper.remove_element_from_html2(td_without_sup, "sup")
                a_list = Scrapper.find_all(td_without_sup, "a")
                for a in a_list:
                    if "cite" not in a:
                        if "<img" not in a:
                            if limba_oficiala == "":
                                limba_oficiala = limba_oficiala + Scrapper.get_inner_text(a)
                                link_limba_oficiala = link_limba_oficiala + Scrapper.get_attribute_value(a, "href")
                            else:
                                limba_oficiala = limba_oficiala + ", " + Scrapper.get_inner_text(a)
                                link_limba_oficiala = link_limba_oficiala + ", " + Scrapper.get_attribute_value(a, "href")
            elif "Etnonim" in tr:
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                td_without_small = Scrapper.remove_exact_element(td_text, "small")
                while "<small" in td_without_small:
                    td_without_small = Scrapper.remove_exact_element(td_without_small, "small")
                if "<img" in td_without_small:
                    td_without_a = Scrapper.remove_element_from_html(td_without_small, "a")
                    etnonime = etnonime + td_without_a.replace(" ", "").replace("<br/>", ", ")
                    etnonime = etnonime.replace(" ", "").replace(",", ", ")
                else:
                    etnonime = etnonime + td_without_small.replace("<br />", ", ")
                    a = Scrapper.find_first(etnonime, "a")
                    a_text = Scrapper.get_inner_text(a)
                    etnonime = Scrapper.remove_element_from_html(etnonime, "a") + a_text
                    etnonime = etnonime.replace(" ", "").replace(",", ", ")
                etnonime = etnonime.split("<")[0].replace("\n", "")
            elif "regionale/minoritare" in tr:
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                a_list = Scrapper.find_all(td_text, "a")
                for a in a_list:
                    if limbi_regionale_minoritate == "":
                        limbi_regionale_minoritate = limbi_regionale_minoritate + Scrapper.get_inner_text(a)
                    else:
                        limbi_regionale_minoritate = limbi_regionale_minoritate + ", " + Scrapper.get_inner_text(a)
        return [limba_oficiala, link_limba_oficiala, etnonime, limbi_regionale_minoritate]

    def get_guvernare_data(self):
        html_text_removed_trouble_table = Scrapper.remove_element_from_html_with_attribute(self.html_text, "table", 0, 'align')
        html_text_removed_trouble_table_2 = Scrapper.remove_exact_element(html_text_removed_trouble_table, "table", 0)
        html_text_removed_trouble_table_3 = Scrapper.remove_exact_element(html_text_removed_trouble_table_2, "table", 0)
        html_text_removed_trouble_table_4 = Scrapper.remove_exact_element(html_text_removed_trouble_table_3, "table", 0)

        table = Scrapper.find_first_with_attribute(html_text_removed_trouble_table_4, "table", 0, 'class="infocaseta"')
        tbody = Scrapper.get_inner_text(table)
        tr_list = Scrapper.find_all(tbody, "tr")
        sistem_politic = ""
        presedinte = ""
        prim_ministru = ""
        link_presedinte = ""
        link_prim_ministru = ""
        for tr in tr_list:
            if "Sistem politic" in tr:
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                a_list = Scrapper.find_all2(td_text, "a")
                for a in a_list:
                    if not "<img" in a:
                        sistem_politic = sistem_politic + "+ " + Scrapper.get_inner_text2(a)
                td_without_a = Scrapper.remove_element_from_html(td_text, "a")
                while "<a" in td_without_a:
                    td_without_a = Scrapper.remove_element_from_html(td_without_a, "a")
                if td_without_a != td_text:
                    sistem_politic = sistem_politic + "/" + td_without_a
                sistem_politic = sistem_politic.replace(",","").replace("/", "").replace("+",",")
                if sistem_politic[0:2] == ', ':
                    sistem_politic = sistem_politic[2:]
                sistem_politic = sistem_politic.split("&")[0]
                if sistem_politic.endswith(", "):
                    sistem_politic = sistem_politic[0: len(sistem_politic)-2]
                sistem_politic = sistem_politic.split("<")[0]
            elif "președinte" in tr.lower() or "president" in tr.lower():
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                a_list = Scrapper.find_all2(td_text,"a")
                a = ""
                for a1 in a_list:
                    if "<img" not in a1:
                        a = a + copy.deepcopy(a1)
                        break
                presedinte = presedinte + Scrapper.get_inner_text2(a)
                if presedinte.startswith("<"):
                    presedinte = Scrapper.get_inner_text2(presedinte)
                link_presedinte = link_presedinte + Scrapper.get_attribute_value(a,"href")
            elif "prim" in tr.lower():
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                a_list = Scrapper.find_all2(td_text, "a")
                a = ""
                for a1 in a_list:
                    if "<img" not in a1:
                        a = a + copy.deepcopy(a1)
                        break
                prim_ministru = prim_ministru + Scrapper.get_inner_text2(a)
                if prim_ministru.startswith("<"):
                    prim_ministru = Scrapper.get_inner_text2(prim_ministru)
                link_prim_ministru = link_prim_ministru + Scrapper.get_attribute_value(a, "href")

        return [sistem_politic, presedinte, link_presedinte, prim_ministru, link_prim_ministru]

    def get_identificatori_data(self):
        html_text_removed_trouble_table = Scrapper.remove_element_from_html_with_attribute(self.html_text, "table", 0,
                                                                                           'align')
        html_text_removed_trouble_table_2 = Scrapper.remove_exact_element(html_text_removed_trouble_table, "table", 0)
        html_text_removed_trouble_table_3 = Scrapper.remove_exact_element(html_text_removed_trouble_table_2, "table", 0)
        html_text_removed_trouble_table_4 = Scrapper.remove_exact_element(html_text_removed_trouble_table_3, "table", 0)

        table = Scrapper.find_first_with_attribute(html_text_removed_trouble_table_4, "table", 0, 'class="infocaseta"')
        tbody = Scrapper.get_inner_text(table)
        tr_list = Scrapper.find_all(tbody, "tr")
        cod_cio = ""
        cod_mobil = ""
        prefix_mobil = ""
        domeniu_internet = ""
        for tr in tr_list:
            if "cio" in tr.lower():
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                th = Scrapper.find_first(tr, "th")
                th_text = Scrapper.get_inner_text(th)
                a = Scrapper.find_first(th_text, "a")
                a_text = Scrapper.get_inner_text(a)
                if "cio" == a_text.lower():
                    td_text_without_a = Scrapper.remove_element_from_html(td_text, "a")
                    cod_cio = cod_cio + td_text_without_a.replace(" ", "")
                cod_cio = cod_cio.split("<")[0]
            elif "cod mobil" in tr.lower():
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                td_text_without_a = Scrapper.remove_element_from_html(td_text, "a")
                cod_mobil = cod_mobil + td_text_without_a.replace(" ", "")
                cod_mobil = cod_mobil.split("<")[0]
            elif "prefix telefonic" in tr.lower():
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                td_text_without_a = Scrapper.remove_element_from_html(td_text, "a")
                prefix_mobil = prefix_mobil + td_text_without_a.replace(" ", "")
                prefix_mobil = prefix_mobil.split("<")[0]
            elif "domeniu internet" in tr.lower():
                td = Scrapper.find_first(tr, "td")
                td_text = Scrapper.get_inner_text(td)
                a = Scrapper.find_first(td_text, "a")
                domeniu_internet = domeniu_internet + Scrapper.get_inner_text(a)
                domeniu_internet = domeniu_internet.split("<")[0]

        return [cod_cio, cod_mobil, prefix_mobil, domeniu_internet]

    def get_economie_data(self):
        html_text_removed_trouble_table = Scrapper.remove_element_from_html_with_attribute(self.html_text, "table", 0, 'align')
        html_text_removed_trouble_table_2 = Scrapper.remove_exact_element(html_text_removed_trouble_table, "table", 0)
        html_text_removed_trouble_table_3 = Scrapper.remove_exact_element(html_text_removed_trouble_table_2, "table", 0)
        html_text_removed_trouble_table_4 = Scrapper.remove_exact_element(html_text_removed_trouble_table_3, "table", 0)

        table = Scrapper.find_first_with_attribute(html_text_removed_trouble_table_4, "table", 0, 'class="infocaseta"')
        tbody = Scrapper.get_inner_text(table)
        tr_list = Scrapper.find_all(tbody, "tr")

        pib_ppc_total = ""
        pib_ppc_cap_locuitor = ""
        pib_nominal_total = ""
        pib_nominal_cap_locuitor = ""
        gini = ""
        idu = ""
        moneda = ""
        nominal_start = False
        economie = False

        for tr in tr_list:
            if "economie" in tr.lower():
                economie = True
            if economie:
                if "(nominal)" in tr.lower():
                    nominal_start = True
                if not nominal_start:
                    if "total" in tr.lower():
                        td = Scrapper.find_first(tr, "td")
                        td_text = Scrapper.get_inner_text(td)
                        td_without_sup = Scrapper.remove_element_from_html3(td_text, "sup")
                        while "<sup" in td_without_sup:
                            td_without_sup = Scrapper.remove_element_from_html3(td_without_sup, "sup")
                        td_without_a = Scrapper.remove_element_from_html3(td_without_sup, "a")
                        while "<a" in td_without_a:
                            td_without_a = Scrapper.remove_element_from_html3(td_without_a, "a")
                        td_without_span = Scrapper.remove_element_from_html3(td_without_a, "span")
                        while "<span" in td_without_span:
                            td_without_span = Scrapper.remove_element_from_html3(td_without_span, "span")
                        td_without_span = td_without_span.split("&")[0].split("(")[0]
                        pib_ppc_total = pib_ppc_total + td_without_span
                        if pib_ppc_total == "":
                            span_list = Scrapper.find_all(td_text, "span")
                            for span in span_list:
                                if "$" in span:
                                    td_without_sup = Scrapper.remove_element_from_html3(span, "sup")
                                    while "<sup" in td_without_sup:
                                        td_without_sup = Scrapper.remove_element_from_html3(td_without_sup, "sup")
                                    pib_ppc_total = pib_ppc_total + Scrapper.get_inner_text(td_without_sup).replace("&#160;", " ")
                        pib_ppc_total = Scrapper.remove_starting_and_ending_spaces(pib_ppc_total).split("<")[0]

                    elif "pe cap de locuitor" in tr.lower():
                        td = Scrapper.find_first(tr, "td")
                        td_text = Scrapper.get_inner_text(td)
                        td_without_sup = Scrapper.remove_element_from_html3(td_text, "sup")
                        while "<sup" in td_without_sup:
                            td_without_sup = Scrapper.remove_element_from_html3(td_without_sup, "sup")
                        td_without_a = Scrapper.remove_element_from_html3(td_without_sup, "a")
                        while "<a" in td_without_a:
                            td_without_a = Scrapper.remove_element_from_html3(td_without_a, "a")
                        td_without_span = Scrapper.remove_element_from_html3(td_without_a, "span")
                        while "<span" in td_without_span:
                            td_without_span = Scrapper.remove_element_from_html3(td_without_span, "span")
                        td_without_span = td_without_span.split("&")[0].split("(")[0]
                        pib_ppc_cap_locuitor = pib_ppc_cap_locuitor + td_without_span
                        if pib_ppc_cap_locuitor == "":
                            span_list = Scrapper.find_all(td_text, "span")
                            for span in span_list:
                                if "$" in span:
                                    td_without_sup = Scrapper.remove_element_from_html3(span, "sup")
                                    while "<sup" in td_without_sup:
                                        td_without_sup = Scrapper.remove_element_from_html3(td_without_sup, "sup")
                                    pib_ppc_cap_locuitor = pib_ppc_cap_locuitor + Scrapper.get_inner_text(td_without_sup).replace("&#160;", " ")
                        pib_ppc_cap_locuitor = Scrapper.remove_starting_and_ending_spaces(pib_ppc_cap_locuitor).split("<")[0]
                else:
                    if "total" in tr.lower():
                        td = Scrapper.find_first(tr, "td")
                        td_text = Scrapper.get_inner_text(td)
                        td_without_sup = Scrapper.remove_element_from_html3(td_text, "sup")
                        while "<sup" in td_without_sup:
                            td_without_sup = Scrapper.remove_element_from_html3(td_without_sup, "sup")
                        td_without_a = Scrapper.remove_element_from_html3(td_without_sup, "a")
                        while "<a" in td_without_a:
                            td_without_a = Scrapper.remove_element_from_html3(td_without_a, "a")
                        td_without_span = Scrapper.remove_element_from_html3(td_without_a, "span")
                        while "<span" in td_without_span:
                            td_without_span = Scrapper.remove_element_from_html3(td_without_span, "span")
                        td_without_span = td_without_span.split("&")[0].split("(")[0]
                        pib_nominal_total = pib_nominal_total + td_without_span
                        if pib_nominal_total == "":
                            span_list = Scrapper.find_all(td_text, "span")
                            for span in span_list:
                                if "$" in span:
                                    td_without_sup = Scrapper.remove_element_from_html3(span, "sup")
                                    while "<sup" in td_without_sup:
                                        td_without_sup = Scrapper.remove_element_from_html3(td_without_sup, "sup")
                                    pib_nominal_total = pib_nominal_total + Scrapper.get_inner_text(td_without_sup).replace("&#160;", " ")
                        pib_nominal_total = Scrapper.remove_starting_and_ending_spaces(pib_nominal_total).split("<")[0]
                    elif "pe cap de locuitor" in tr.lower():
                        td = Scrapper.find_first(tr, "td")
                        td_text = Scrapper.get_inner_text(td)
                        td_without_sup = Scrapper.remove_element_from_html3(td_text, "sup")
                        while "<sup" in td_without_sup:
                            td_without_sup = Scrapper.remove_element_from_html3(td_without_sup, "sup")
                        td_without_a = Scrapper.remove_element_from_html3(td_without_sup, "a")
                        while "<a" in td_without_a:
                            td_without_a = Scrapper.remove_element_from_html3(td_without_a, "a")
                        td_without_span = Scrapper.remove_element_from_html3(td_without_a, "span")
                        while "<span" in td_without_span:
                            td_without_span = Scrapper.remove_element_from_html3(td_without_span, "span")
                        td_without_span1 = td_without_span.split("&")[0].split("(")[0]
                        if td_without_span == "":
                            td_without_span = td_without_span.split("&")[0].replace("(", "").replace(")","")
                        if td_without_span1 != "":
                            pib_nominal_cap_locuitor = pib_nominal_cap_locuitor + td_without_span1
                        else:
                            pib_nominal_cap_locuitor = pib_nominal_cap_locuitor + td_without_span
                        if pib_nominal_cap_locuitor == "":
                            span_list = Scrapper.find_all(td_text, "span")
                            for span in span_list:
                                if "$" in span:
                                    td_without_sup = Scrapper.remove_element_from_html3(span, "sup")
                                    while "<sup" in td_without_sup:
                                        td_without_sup = Scrapper.remove_element_from_html3(td_without_sup, "sup")
                                    pib_nominal_cap_locuitor = pib_nominal_cap_locuitor + Scrapper.get_inner_text(td_without_sup).replace("&#160;", " ")
                        pib_nominal_cap_locuitor = Scrapper.remove_starting_and_ending_spaces(pib_nominal_cap_locuitor).split("<")[0]
                        pib_nominal_cap_locuitor = pib_nominal_cap_locuitor.replace("()","").replace("&#32;","")
                if "gini" in tr.lower():
                    td = Scrapper.find_first(tr, "td")
                    td_text = Scrapper.get_inner_text(td)
                    td_without_sup = Scrapper.remove_element_from_html3(td_text, "sup")
                    while "<sup" in td_without_sup:
                        td_without_sup = Scrapper.remove_element_from_html3(td_without_sup, "sup")
                    td_without_a = Scrapper.remove_element_from_html3(td_without_sup, "a")
                    while "<a" in td_without_a:
                        td_without_a = Scrapper.remove_element_from_html3(td_without_a, "a")
                    td_without_span = Scrapper.remove_element_from_html3(td_without_a, "span")
                    while "<span" in td_without_span:
                        td_without_span = Scrapper.remove_element_from_html3(td_without_span, "span")
                    td_without_span = td_without_span.split("&")[0].split("(")[0]
                    gini = gini + td_without_span.split("<")[0]
                    gini = Scrapper.remove_starting_and_ending_spaces(gini)

                elif "idu" in tr.lower():
                    td = Scrapper.find_first(tr, "td")
                    td_text = Scrapper.get_inner_text(td)
                    td_without_sup = Scrapper.remove_element_from_html3(td_text, "sup")
                    while "<sup" in td_without_sup:
                        td_without_sup = Scrapper.remove_element_from_html3(td_without_sup, "sup")
                    td_without_a = Scrapper.remove_element_from_html3(td_without_sup, "a")
                    while "<a" in td_without_a:
                        td_without_a = Scrapper.remove_element_from_html3(td_without_a, "a")
                    td_without_span = Scrapper.remove_element_from_html3(td_without_a, "span")
                    while "<span" in td_without_span:
                        td_without_span = Scrapper.remove_element_from_html3(td_without_span, "span")
                    td_without_span = td_without_span.split("&")[0].split("(")[0]
                    idu = idu + td_without_span.split("<")[0]
                    idu = Scrapper.remove_starting_and_ending_spaces(idu)
                elif "moned" in tr.lower():
                    td = Scrapper.find_first(tr, "td")
                    td_text = Scrapper.get_inner_text(td)
                    td_without_sup = Scrapper.remove_element_from_html3(td_text, "sup")
                    a_value = Scrapper.get_inner_text(Scrapper.find_first(td_without_sup, "a"))
                    while "<sup" in td_without_sup:
                        td_without_sup = Scrapper.remove_element_from_html3(td_without_sup, "sup")
                    td_without_a = Scrapper.remove_element_from_html3(td_without_sup, "a")
                    while "<a" in td_without_a:
                        td_without_a = Scrapper.remove_element_from_html3(td_without_a, "a")
                    td_without_span = Scrapper.remove_element_from_html3(td_without_a, "span")
                    while "<span" in td_without_span:
                        td_without_span = Scrapper.remove_element_from_html3(td_without_span, "span")
                    td_without_span = td_without_span.split("&")[0]
                    moneda = moneda + td_without_span
                    moneda = a_value + " " + moneda.replace("()","").split("<")[0]
                    moneda = Scrapper.remove_starting_and_ending_spaces(moneda)
                    if "hiperinflației" in moneda:
                        moneda = "dolarul american, randul sud-african, pula botswaneză, lira sterlină și Euro"

        return [pib_ppc_total, pib_ppc_cap_locuitor, pib_nominal_total, pib_nominal_cap_locuitor, gini, idu, moneda]


if __name__ == "__main__":
    obtain = OtherDetailsDataObtainer()
    obtain.get_html_text("/wiki/Muntenegru")
    guvernare = obtain.get_economie_data()
    print(guvernare)
