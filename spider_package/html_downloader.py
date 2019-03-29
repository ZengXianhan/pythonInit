import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is not None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            return response.read()
        else:
            return None