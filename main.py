from downloader import *

URL = 'http://www.nyaa.se/'
TEST= '[Chihiro-Amaterasu]_Rewrite_-_04_[720P_Hi10P_AAC][CA993780]'
TESTLINK = 'www.nyaa.se/?page=download&amp;tid=853638'

html = getHTML(URL)
download_episode(html,TEST)