#!/usr/bin/env python
from downloader import *
from searcher import *
import schedule
import time


#URL = 'http://www.nyaa.se'
URL = 'http://www.nyaa.se/?page=search&cats=0_0&filter=0&term=WWW.wor'
TEST= '[HorribleSubs] Active Raid S2 - 12 [720p].mkv'
TESTLINK = 'http://www.nyaa.se/?page=download&tid=855918'
TESTFILE= 'E:\Projects\Episode-Bot\downloads\[HorribleSubs] Mobile Suit Gundam - Iron-Blooded Orphans S2 - 01 [1080p].mkv.torrent'
TESTTITLE = 'WWW.Working!!'


count = 0

print('Start')

def job():
    print('--------------------------------------------------------------------------------')
    global count
    count+= 1
    print('Booting up...' + str(count))
    html = getHTML(URL)
    search('season_conf/watch_list', html)
    print('Done')

schedule.every(60).minutes.do(stop_seed)
schedule.every(3).minutes.do(job)

job()

while True:
    schedule.run_pending()
    time.sleep(1)
