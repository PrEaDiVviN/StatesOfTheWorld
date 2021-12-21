import copy


class Scrapper:

    @staticmethod
    def find_first(html_text, element_html, position_cursor=0):
        start_index = position_cursor
        found = False
        while start_index != -1 or not found:
            start_index = html_text.find("<" + element_html, start_index)
            if start_index != -1:
                if html_text[start_index + len(element_html) + 1] in " >":
                    finish_index = html_text.find("</" + element_html + ">", start_index)
                    if finish_index != -1:
                        return html_text[start_index: finish_index + len(element_html) + 3]
                else:
                    start_index = start_index + 1
            else:
                found = True
        return ""

    @staticmethod
    def get_inner_text(element_html_text):
        start_element = element_html_text.find(">")
        end_element = element_html_text.rfind("<", start_element + 1)
        if start_element != -1 and end_element != -1:
            return element_html_text[start_element+1: end_element]
        return ""

    @staticmethod
    def find_all(html_text, element_html, position_cursor=0):
        elements = list()
        start_index = position_cursor
        keep_going = True
        while keep_going:
            start_index = html_text.find("<" + element_html, start_index)
            if start_index != -1:
                element = Scrapper.find_first(html_text, element_html, start_index)
                elements.append(copy.deepcopy(element))
                start_index = start_index + 1
            else:
                keep_going = False
        return elements

    @staticmethod
    def get_attribute_value(element_html_text, attribute_name):
        start_attribute = element_html_text.find(attribute_name)
        if start_attribute != -1:
            start_attribute = start_attribute + len(attribute_name) + len(" #")
            end_attribute = element_html_text.find("\"", start_attribute)
            return element_html_text[start_attribute : end_attribute]
        return ""

    @staticmethod
    def get_substring_from_item(html_text, item):
        start_item = html_text.rfind(item)
        return html_text[start_item:]

    @staticmethod
    def get_substring_from_item_till_end(html_text, item_end):
        end_item = html_text.find(item_end)
        return html_text[0:end_item]

    @staticmethod
    def remove_element_from_html(html_text, element_html):
        start_element = html_text.find("<" + element_html)
        end_element = html_text.find("</" + element_html + ">")
        if start_element - 1 > 0 and end_element != -1:
            return html_text[0:start_element-1] + html_text[end_element + len(element_html) + 3:]
        else:
            if start_element != -1 and end_element != -1:
                return html_text[end_element + len(element_html) + 3:]
            return ""