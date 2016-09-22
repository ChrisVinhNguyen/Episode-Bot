from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

HOMEPAGE = 'http://www.nyaa.se/'

def download_episode(html_string):
    html = BeautifulSoup(html_string, 'html.parser')
    print(html.a.get_text())


html_string = ''
try:
    response = urlopen(HOMEPAGE)
    if 'text/html' in response.getheader('Content-Type'):
        html_bytes = response.read()
        html_string = html_bytes.decode("utf-8")
    download_episode(html_string)
except Exception as e:
    print(str(e))



