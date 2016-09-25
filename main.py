from downloader import *

URL = 'http://www.nyaa.se/'
TEST= '[HorribleSubs] Bonobono - 25 [1080p].mkv'

html = getHTML(URL)
download_episode(html,TEST)