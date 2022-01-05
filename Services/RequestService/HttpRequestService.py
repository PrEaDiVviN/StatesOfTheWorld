import urllib.request as request


class HttpRequestService:
    """ A wrapping used to handle Http requests. """

    @staticmethod
    def get_html_from_request(url):
        """ A function used to make an http request on a specified url and get is text, decode is as utf-8
        and return it.

        :param url: Url to request from
        :return: Html text from url decoded as utf-8
        """
        context_manager = request.urlopen(url)
        return context_manager.read().decode('utf-8')
