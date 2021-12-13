import copy
import urllib.request as request


def get_string_from_url(url):
    context_manager = request.urlopen(url)
    return context_manager.read().decode('utf-8')


def get_table_body(parse_string):
    tag_start = "<tbody>"
    tag_end = "</tbody>"
    pos_start = parse_string.find(tag_start)
    pos_end = parse_string.find(tag_end)
    table_data = parse_string[pos_start:pos_end + len(tag_end)]
    return table_data


def print_country_name_and_links(table_data):
    split_lines = table_data.split('<tr valign="top">')
    for i in range(1, len(split_lines)):
        # obtinerea numelor si link-urilor pentru tara respectiva
        split_anchor = split_lines[i].split("<a")
        end = split_anchor[1].find("</a>")
        anchor_data = split_anchor[1][0:end+1]
        country_name = anchor_data[anchor_data.find(">") + 1: anchor_data.find("<")]
        country_link = anchor_data[anchor_data.find('href="') + len('href="'): anchor_data.find('" ')]
        print(country_name, country_link)


def print_country_name_and_links_and_capitals(table_data):
    split_lines = table_data.split('<tr')
    for i in range(2, len(split_lines)):
        capital_column_data = split_lines[i].split('<td')[5]
        start_capitale = capital_column_data.find("<i>")
        end_capitale = capital_column_data.find("</p>", start_capitale)
        capitala_string = capital_column_data[start_capitale + 1: end_capitale]
        capitala_anchor = ""
        list_capitals = list()
        if "Capitala" in capitala_string or "Capitală" in capitala_string:
            a_start = capitala_string.find("<a")
            a_end = capitala_string.find("</a>")
            capitala_anchor = capitala_string[a_start+1: a_end]
            capitala_anchor = capitala_anchor.split(">")[1]
        else:
            look_for_capitals = 0
            a_start = 0
            a_end = 0
            while look_for_capitals != -1:
                a_start = capitala_string.find("<a", a_start)
                a_end = capitala_string.find("</a>", a_end)
                if a_start != -1 and a_end != -1:
                    capitala_anchor = capitala_string[a_start + 1: a_end]
                    capitala_noua = capitala_anchor.split(">")
                    capitala = capitala_noua[1]
                    list_capitals.append(capitala)
                    a_start = a_start + 1
                    a_end = a_end + 1
                else:
                    look_for_capitals = -1
            capitala_anchor = ""
            # print(list_capitals)
        # obtinerea numelor si link-urilor pentru tara respectiva
        split_b = split_lines[i].split("<b")[1]
        split_anchor = split_b.split("<a")
        end = split_anchor[1].find("</a>")
        anchor_data = split_anchor[1][0:end+1]
        country_name = anchor_data[anchor_data.find(">") + 1: anchor_data.find("<")]
        country_link = anchor_data[anchor_data.find('href="') + len('href="'): anchor_data.find('" ')]
        if capitala_anchor != "":
            print(country_name, capitala_anchor, country_link)
        else:
            print(country_name, list_capitals, country_link)



url_data = get_string_from_url("https://ro.wikipedia.org/wiki/Lista_statelor_lumii")
table_body = get_table_body(url_data)
# print_country_name_and_links(table_body)
print_country_name_and_links_and_capitals(table_body)

