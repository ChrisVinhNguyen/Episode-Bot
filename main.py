#!/usr/bin/env python
from downloader import *
from searcher import *
import schedule
import time


URL = 'http://www.nyaa.se/'
URLHorribleSubs = 'http://www.nyaa.se/?page=search&cats=0_0&filter=0&term=horriblesubs'
URLFilter = 'http://www.nyaa.se/?page=search&cats=0_0&filter=0&term='


count = 0

print('Start')

def job():
    print('-----------------------------------------------------------------')
    global count
    count+= 1
    print('Booting up...' + str(count))
    html = getHTML(URL)
    search('season_conf/watch_list', html)
    print('Done')

def job2():
	print('scanning HorribleSubs')
	html = getHTML(URLHorribleSubs)
	search('season_conf/watch_list', html)
	print('Done')

def job3(searchterm):
	print('scanning for ' + searchterm)
	URLsearch = URLFilter + searchterm
	html = getHTML(URLsearch)
	search('season_conf/watch_list', html)
	print('Done')

schedule.every(60).minutes.do(stop_seed)
schedule.every(15).minutes.do(job)

job()
job2()

while True:
	schedule.run_pending()
	time.sleep(1)
	searchterm = input('Enter search term: ')
	if searchterm:
		job3(searchterm)
	else:
		print('invalid')
    

