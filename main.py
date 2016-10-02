from downloader import *
from searcher import *
import schedule
import time

URL = 'http://www.nyaa.se/'
TEST= '[HorribleSubs] Active Raid S2 - 12 [720p].mkv'
TESTLINK = 'http://www.nyaa.se/?page=download&tid=855452'
TESTFILE= 'downloads/qwrqwsrqw.torrent'

print('Start')

def job():
    print('---------------------------------------------------------------------------------------------------------------')
    print('Booting up...')
    html = getHTML(URL)
    search('season_conf/watch_list', html)
    print('Shutting down...')

schedule.every(3).minutes.do(job)

while True:
    schedule.run_pending()
    #time.sleep(1)

