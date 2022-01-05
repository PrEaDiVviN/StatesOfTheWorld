import copy


class Scrapper:
    """A class implementing basic scrapping functionalities"""

    @staticmethod
    def find_first(html_text, element_html, position_cursor=0):
        """ A function that finds the first occurrence of a specified html element in a html string given a position to
        start the searching on or empty string if not found.

        :param html_text: Html as string
        :param element_html: Element html as string (only it's name)
        :param position_cursor: Position to start the searching (default = 0)
        :return: Specified element as string or empty string if not found
        """
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
    def find_first_with_attribute(html_text, element_html, position_cursor=0, attribute=""):
        """ A function that finds the first occurrence of a specified html element in a html string given a position to
        start the searching on and a specified first attribute to contain or empty string if not found.

        :param html_text: Html as string
        :param element_html: Element html as string (only it's name)
        :param position_cursor: Position to start the searching (default 0)
        :param attribute: Html attribute as string
        :return: Specified element as string or empty string if not found
        """
        start_index = position_cursor
        found = False
        while start_index != -1 or not found:
            start_index = html_text.find('<' + element_html + ' ' + attribute, start_index)
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
        """ A function that removes the wrapping html element from the html text or empty string if not found.

        :param element_html_text: Html text as string
        :return: Html text as string by removing wrapping html element or empty string if not found
        """
        start_element = element_html_text.find(">")
        end_element = element_html_text.rfind("<", start_element + 1)
        if start_element != -1 and end_element != -1:
            return element_html_text[start_element+1: end_element]
        return ""

    @staticmethod
    def get_inner_text2(element_html_text):
        """ A function that removes the wrapping html element from the html text.

        :param element_html_text: Html text as string
        :return: Html text as string by removing wrapping html element
        """
        start_element = element_html_text.find(">")
        end_element = element_html_text.rfind("<", start_element + 1)
        if start_element != -1 and end_element != -1:
            return element_html_text[start_element+1: end_element]
        return element_html_text

    @staticmethod
    def find_all(html_text, element_html, position_cursor=0):
        """ A function that finds all occurrences of a specified html element given a position to start in the html
        text or empty string if not found.

        :param html_text: Html text as string
        :param element_html: Html element as string (only its name)
        :param position_cursor: position to start on (default 0)
        :return: List of all occurrences of specified element in the Html text or Empty list if none found
        """
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
    def find_all2(html_text, element_html, position_cursor=0):
        """ A function that finds all occurrences of a specified html element given a position to start in the html
        text or a list containing initial html text if not found.

        :param html_text: Html text as string
        :param element_html: Html element as string (only its name)
        :param position_cursor: position to start on (default 0)
        :return: List of all occurrences of specified element in the Html text or a list containing initial html text
        if not found
        """
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
        if len(elements) == 0:
            return [html_text]
        return elements

    @staticmethod
    def get_attribute_value(element_html_text, attribute_name):
        """ A function that returns the value of a specified attribute from the current top level html element
        or empty string if not found.

        :param element_html_text: Element html as string
        :param attribute_name: Attribute html as string
        :return: The value of a specified attribute from top level html element or empty string if not found
        """
        start_attribute = element_html_text.find(attribute_name)
        if start_attribute != -1:
            start_attribute = start_attribute + len(attribute_name) + len(" #")
            end_attribute = element_html_text.find("\"", start_attribute)
            return element_html_text[start_attribute : end_attribute]
        return ""

    @staticmethod
    def get_substring_from_item(html_text, item):
        """ A function that returns a substring of a string by finding the last position of a specified string to the
        end of the string.

        :param html_text: Html text as string
        :param item: Item as string
        :return: Substring from item to end of string
        """
        start_item = html_text.rfind(item)
        return html_text[start_item:]

    @staticmethod
    def get_substring_from_item_till_end(html_text, item_end):
        """  A function that returns a substring of a string by finding the first position of a specified string and
        starting from 0 to that position exclusive.

        :param html_text:
        :param item_end:
        :return:
        """
        end_item = html_text.find(item_end)
        if end_item == -1:
            return html_text
        return html_text[0:end_item]

    @staticmethod
    def remove_element_from_html(html_text, element_html, start=0):
        """ A function that removes a specified html element from a html string starting on a specified position.

        :param html_text: Html text as string
        :param element_html: Html element as string
        :param start: starting position (default 0)
        :return: Html text from which the element is removed
        """
        start_element = html_text.find("<" + element_html, start)
        end_element = html_text.find("</" + element_html + ">", start_element)
        if start_element - 1 > 0 and end_element != -1:
            return html_text[0:start_element-1] + html_text[end_element + len(element_html) + 3:]
        else:
            if start_element != -1 and end_element != -1:
                return html_text[end_element + len(element_html) + 3:]
            return html_text

    @staticmethod
    def remove_element_from_html2(html_text, element_html, start=0):
        """ A function that removes a specified html element from a html string starting on a specified position.

        :param html_text: Html text as string
        :param element_html: Html element as string
        :param start: starting position (default 0)
        :return: Html text from which the element is removed
        """
        start_element = html_text.find("<" + element_html, start)
        end_element = html_text.find("</" + element_html + ">", start_element)
        if start_element - 1 > 0 and end_element != -1:
            return html_text[0:start_element-1] + html_text[end_element + len(element_html) + 2:]
        else:
            if start_element != -1 and end_element != -1:
                return html_text[end_element + len(element_html) + 3:]
            return html_text

    @staticmethod
    def remove_element_from_html3(html_text, element_html, start=0):
        """ A function that removes a specified html element from a html string starting on a specified position.

        :param html_text: Html text as string
        :param element_html: Html element as string
        :param start: starting position (default 0)
        :return: Html text from which the element is removed
        """
        start_element = html_text.find("<" + element_html, start)
        end_element = html_text.find("</" + element_html + ">", start_element)
        if start_element - 1 > 0 and end_element != -1:
            return html_text[0:start_element] + html_text[end_element + len(element_html) + 3:]
        else:
            if start_element != -1 and end_element != -1:
                return html_text[end_element + len(element_html) + 3:]
            return html_text

    @staticmethod
    def remove_element_from_html_with_attribute(html_text, element_html, start=0, attribute=""):
        """ A function that removes a specified html element from a html string starting on a specified position which
        contains a specified attribute or empty string if not found.

        :param html_text: Html text as string
        :param element_html: Html element as string
        :param start: starting position (default 0)
        :return: Html text from which the element is removed or or empty string if not found.
        """
        start_element = html_text.find("<" + element_html + " " + attribute, start)
        end_element = html_text.find("</" + element_html + ">", start_element)
        if start_element - 1 > 0 and end_element != -1:
            return html_text[0:start_element-1] + html_text[end_element + len(element_html) + 3:]
        else:
            if start_element != -1 and end_element != -1:
                return html_text[end_element + len(element_html) + 3:]
            return ""
    @staticmethod
    def remove_exact_element(html_text, element_html, start=0):
        """ A function that removes a specified html element from a html string starting on a specified position which
        does not contain any attributes or the initial html text if not found.

        :param html_text: Html text as string
        :param element_html: Html element as string
        :param start: starting position (default 0)
        :return: Html text from which the element is removed or the initial html text if not found.
        """
        start_element = html_text.find("<" + element_html + ">", start)
        end_element = html_text.find("</" + element_html + ">", start_element)
        if start_element - 1 > 0 and end_element != -1:
            return html_text[0:start_element-1] + html_text[end_element + len(element_html) + 3:]
        else:
            if start_element != -1 and end_element != -1:
                return html_text[end_element + len(element_html) + 3:]
            return html_text

    @staticmethod
    def get_text_between_separators(text, start_sep, end_sep):
        """ A function that get the substring from specified string separators: inclusive, exclusive.

        :param text: Text to get substring from
        :param start_sep: Starting separator
        :param end_sep: Ending separator
        :return: substring from specified string separators:
        """
        start_pos = text.find(start_sep)
        end_pos = text.find(end_sep, start_pos)
        return text[start_pos:end_pos]

    @staticmethod
    def remove_starting_and_ending_spaces(text):
        """ A function that removes all the spaces from the start and from the end of the string.

        :param text: Text to remove from
        :return: Text from which starting and ending spaces were removed
        """
        if len(text) > 0:
            while text[0] == " ":
                text = text[1:]
            while text[len(text)-1] == " ":
                text = text[0: len(text)-1]
        return text
