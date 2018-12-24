import re
import requests
import urllib.request
#urllib.request.urlretrieve(url, "video.mp4")

def get_down_url(url):
    # change 'www' to 'mbasic' in the url
    temp_url = re.sub(r'\bwww\b', 'mbasic', url)
    html = requests.get(temp_url).text
    
    # regex to get downloadable url
    down_url = re.findall('<a href="/video_redirect/(.*?)"', html)

    return requests.get('https://mbasic.facebook.com/video_redirect/' + down_url[0]).url

def uncrypt_url(url):
    h1 = re.findall('https%253A%252F%252F(.*?)%', url)[0]
    h1_2 = re.findall('(.*?).fbc', h1)[0]
    h2 = re.findall('%252Fv%252F(.*?)%', url)[0]
    h3 = re.findall(f'{h2}%252F(.*?)_n.mp4', url)[0]
    h4 = re.findall('_nc_cat%253D(.*?)%', url)[0]
    h5 = re.findall('253Dey(.*?)%', url)[0]
    h6 = re.findall('oh%253D(.*?)%',url)[0]
    h7 = re.findall('oe%253D(.*?)%', url)[0]
    
    return f'https://{h1}/v/{h2}/{h3}_n.mp4?_nc_cat={h4}&efg=ey{h5}&_nc_ht={h1_2}&oh={h6}&oe={h7}'

def download_by_url(url, file_name, path=None):
    if requests.get(url).status_code == 200:
        print("start download")
        urllib.request.urlretrieve(url, file_name)
        print("end download")

def teste(url, file_name):
        raw = requests.get(url, stream=True).raw
        buffer = raw.read(1024)
        print("start download")
        with open(file_name, "wb") as f:
                while(buffer):
                        f.write(buffer)
                        buffer = raw.read(1024)
        print("end download")

url = 'https://www.facebook.com/MomentosdoPassado/videos/1685359324858999/'
download_link = get_down_url(url)

#print(download_link)
# requests.get(url, stream=True)

final_url = uncrypt_url(download_link)
print(final_url)

if requests.get(final_url).status_code == 200:
        teste(final_url, "new_video.mp4")
else:
        print("Fail")
        print(final_url)

#https://mbasic.facebook.com/login.php?next=https%3A%2F%2Fmbasic.facebook.com%2Fvideo_redirect%2F%3Fsrc%3Dhttps%253A%252F%252Fscontent-gru2-1.xx.fbcdn.net%252Fv%252Ft42.9040-4%252F47934099_1976697172451390_106889405146333184_n.mp4%253F_nc_cat%253D1%2526efg%253DeyJ2ZW5jb2RlX3RhZyI6InN2ZV9zZCJ9%2526_nc_ht%253Dscontent-gru2-1.xx%2526oh%253D576f6de0ce248c882f90416a43528448%2526oe%253D5C0B0C7D%26amp%253Bsource%3Dmisc%26amp%253Bid%3D301189540492261%26amp%253Brefid%3D52%26amp%253B__tn__%3DFH-R&refsrc=https%3A%2F%2Fmbasic.facebook.com%2Fvideo_redirect%2F&_rdr

#https://scontent-gru2-1.xx.fbcdn.net/v/t42.9040-4/47934099_1976697172451390_106889405146333184_n.mp4?_nc_cat=1&efg=eyJ2ZW5jb2RlX3RhZyI6InN2ZV9zZCJ9&_nc_ht=scontent-gru2-1.xx&oh=576f6de0ce248c882f90416a43528448&oe=5C0B0C7D'

# https://{scontent||video}-gru2-1.xx.fbcdn.net/v/t42.{dddd}-{d}/{ddddddddd}_{ddddddd}_{dddddd}_n.mp4?_nc_cat={d}&efg=ey{xxxxxxxxxxxxxx}&_nc_ht={scontent||video}-gru2-1.xx&oh={xxxxxxxxxxxx}&oe={xxxxxxx}

#download_by_url(download_link, "test2.mp4")

# PATH:
# <a href="/video_redirect/
