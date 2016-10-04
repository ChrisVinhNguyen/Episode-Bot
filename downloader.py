from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import requests
from requests import get
import os
from qbittorrent import Client
import cfscrape


def find_episode(html_string,title,source,quality , episode):
    html = BeautifulSoup(html_string, 'html.parser')
    found = False
    title = re.compile(title)
    source = re.compile(source)
    quality = re.compile(quality)
    episode = re.compile(episode)
    elements = (html.find_all('a', text=title))
    elements2 = (html.find_all('a',text=source))
    elements3 = (html.find_all('a',text=quality))
    elements4 = (html.find_all('a',text=episode))

    for element1 in elements:
        for element2 in elements2:
            for element3 in elements3:
                for element4 in elements4:
                    if element1 == element2 == element3 == element4:
                        element = element1
                        found = True
                        break

    if not found:
        error = 'error, not found'
        #print(error)
        return error
    #print(elements)
    #print(elements2)
    #print(elements3)
    #print(elements4)
    #print(element)
    link = element.get('href')
    link = link.replace('view','download')
    link = link.replace('//','http://')
    print('Found link --------> ' + link)
    return link


def getHTML(url):
    scraper = cfscrape.create_scraper()
    page = scraper.get(url,auth=('user','pass'))
    html_contents = page.text
    #print (html_contents)
    return html_contents

def has_link(tag):
    return tag.has_attr('href')

def download_episode(download_link,file_name):
    scraper = cfscrape.create_scraper()
    with open(file_name, "wb") as file:
        # get request
        response = scraper.get(download_link)
        # write to file
        file.write(response.content)

def download_torrent(torrent_name,show_name, season,file_name):
    qb = Client(url='http://localhost:8080')

    qb.login('admin','cn101596')
    dl_path = 'E:\Anime 2\\' + file_name + '\\' + 'S' +str(season)
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
    print('Stopping seeds')

def create_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)
