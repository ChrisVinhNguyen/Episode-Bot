from downloader import *
from watchinglist import *

URL = 'http://www.nyaa.se/'
TEST= '[HorribleSubs] Active Raid S2 - 12 [720p].mkv'
TESTLINK = 'http://www.nyaa.se/?page=download&tid=853946'
TESTFILE= 'downloads/test2.torrent'

html = getHTML(URL)
print(find_episode(html,TEST))
download_episode(TESTLINK,TESTFILE)

load_yaml('season_conf/watch_list')
