from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def download_episode(html_string,episode):
    html = BeautifulSoup(html_string, 'html.parser')
    element= (html.find('a', text= episode))
    print(element)
    link = element.get('href')
    link.replace('view','download')
    print(link)


def getHTML(url):
    html_string = ''
    try:
        response = urlopen(url)
        if 'text/html' in response.getheader('Content-Type'):
            html_bytes = response.read()
            html_string = html_bytes.decode("utf-8")
    except Exception as e:
        print(str(e))
    return html_string

def has_link(tag):
    return tag.has_attr('href')
