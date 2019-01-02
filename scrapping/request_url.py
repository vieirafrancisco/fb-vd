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
        #regular expressions list that's need to uncrypt the url
        regex_points = ['https%253A%252F%252F(.*?)%', '%252Fv%252F(.*?)%', '-[0-9]%252F(.*?)_n.mp4',
        '_nc_cat%253D(.*?)%', '253Dey(.*?)%','https%253A%252F%252F(.*?).fbc' ,'oh%253D(.*?)%', 'oe%253D(.*?)%']

        #url static parts list
        url_points = ['https://','/v/','/','_n.mp4?_nc_cat=','&efg=ey','&_nc_ht=','&oh=','&oe=']

        #final url
        url_in_form = ''

        #interate the lists and concat theirs itens
        for u_point, r_point in zip(url_points, regex_points):
            url_in_form += str(u_point + re.findall(r_point, url)[0])

        return url_in_form

    def get_url(self):
        return self._url
