from downloader import *

URL = 'http://www.nyaa.se/'
TEST= '[HorribleSubs] Active Raid S2 - 12 [720p].mkv'
TESTLINK = 'http://www.nyaa.se/?page=download&tid=853946'
TESTFILE= 'downloads/test.torrent'

html = getHTML(URL)
find_episode(html,TEST)
download_episode(TESTLINK,TESTFILE)