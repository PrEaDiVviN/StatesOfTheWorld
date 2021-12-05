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


url_data = get_string_from_url("https://ro.wikipedia.org/wiki/Lista_statelor_lumii")
table_body = get_table_body(url_data)
print(table_body)
