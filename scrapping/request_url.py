import re
import requests
import urllib.request

class Url:
    def __init__(self, link):
        self.link = link

    def _downloadable_url(self):
        # change 'www' to 'mbasic' in the url
        temp_url = re.sub(r'\bwww\b', 'mbasic', url)
        html = requests.get(temp_url).text

        # regex to get downloadable url
        down_url = re.findall('<a href="/video_redirect/(.*?)"', html)