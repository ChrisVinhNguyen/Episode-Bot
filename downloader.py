from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib
from requests import get
import os
from qbittorrent import Client


def find_episode(html_string,episode):
    html = BeautifulSoup(html_string, 'html.parser')
    element= (html.find('a', text=episode))
    if not element:
        error = 'error, not found'
        return error

    link = element.get('href')
    link = link.replace('view','download')
    link = link.replace('//','http://')
    print('Found link --------> ' + link)
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

def download_torrent(torrent_name,show_name, season):
    qb = Client(url='http://localhost:8080')

    qb.login('admin','cn101596')
    dl_path = 'E:\Anime 2\\' + show_name + '\\' + 'S' +str(season)
    create_dir(dl_path)
    torrent_file = open(torrent_name,'rb')
    qb.download_from_file(torrent_file,dl_path)

    torrents = qb.torrents()
    for torrent in torrents:
        print ('downloading.......' + torrent['name'])

def stop_seed():
    qb = Client(url='http://localhost:8080')
    qb.login('admin','cn101596')
    qb.pause_all()

def create_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)
