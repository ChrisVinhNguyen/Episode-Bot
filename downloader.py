from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
from requests import get


def find_episode(html_string,episode):
    html = BeautifulSoup(html_string, 'html.parser')
    element= (html.find('a', text= episode))
    if not element:
        error = 'error'
        return error
    print(element)
    link = element.get('href')
    link = link.replace('view','download')
    return link


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

def download_episode(download_link,file_name):
    with open(file_name, "wb") as file:
        # get request
        response = get(download_link)
        # write to file
        file.write(response.content)

def opentorrent(filename):
    output = open(filename, 'wb')
    output.write(filename.read())
