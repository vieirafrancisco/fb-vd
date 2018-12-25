import re
import requests

from .url_exception import URLException

class Url:
    def __init__(self, link):
        self.link = link
        self._url = self._downloadable_url()

    def _downloadable_url(self):
        # change 'www' to 'mbasic' in the url
        try:
            temp_url = re.sub(r'\bwww\b', 'mbasic', self.link)
            html = requests.get(temp_url).text
        except:
            raise URLException("error: can't substitute 'www' for 'mbasic'")

        # regex to get downloadable url
        try:
            down_url = re.findall('<a href="/video_redirect/(.*?)"', html)
        except:
            raise URLException("error: can't regex to get downloadable url")

        # scrapping the down_url to get the downloadble url
        try:
            return self._uncrypt_url(requests.get('https://mbasic.facebook.com/video_redirect/' + down_url[0]).url)
        except:
            raise URLException("error: can't uncrypt url")

    def _uncrypt_url(self, url):
        h1 = re.findall('https%253A%252F%252F(.*?)%', url)[0]
        h1_2 = re.findall('(.*?).fbc', h1)[0]
        h2 = re.findall('%252Fv%252F(.*?)%', url)[0]
        h3 = re.findall(f'{h2}%252F(.*?)_n.mp4', url)[0]
        h4 = re.findall('_nc_cat%253D(.*?)%', url)[0]
        h5 = re.findall('253Dey(.*?)%', url)[0]
        h6 = re.findall('oh%253D(.*?)%',url)[0]
        h7 = re.findall('oe%253D(.*?)%', url)[0]
    
        return f'https://{h1}/v/{h2}/{h3}_n.mp4?_nc_cat={h4}&efg=ey{h5}&_nc_ht={h1_2}&oh={h6}&oe={h7}'

    def get_url(self):
        return self._url
