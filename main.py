from downloader import *
from searcher import *

URL = 'http://www.nyaa.se/'
TEST= '[HorribleSubs] Active Raid S2 - 12 [720p].mkv'
TESTLINK = 'http://www.nyaa.se/?page=download&tid=855452'
TESTFILE= 'downloads/qwrqwsrqw.torrent'

html = getHTML(URL)
#print(find_episode(html,TEST))
#download_episode(TESTLINK,TESTFILE)


search('season_conf/watch_list',html)


#for show in list:
   #show.find_episodes(html)