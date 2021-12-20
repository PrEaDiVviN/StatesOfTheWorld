import urllib.request as request


class HttpRequestService:

    @staticmethod
    def get_html_from_request(url):
        context_manager = request.urlopen(url)
        return context_manager.read().decode('utf-8')
