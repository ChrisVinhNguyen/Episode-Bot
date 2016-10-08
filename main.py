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

def run():
    print('-----------------------------------------------------------------')
    global count
    count+= 1
    print('Booting up...' + str(count))
    html = getHTML(URL)
    search('season_conf/watch_list', html)
    print('Done')

def hsub():
	print('scanning HorribleSubs')
	html = getHTML(URLHorribleSubs)
	search('season_conf/watch_list', html)
	print('Done')

def searchfor(searchterm):
	print('scanning for ' + searchterm)
	URLsearch = URLFilter + searchterm
	html = getHTML(URLsearch)
	search('season_conf/watch_list', html)
	print('Done')

schedule.every(60).minutes.do(stop_seed)
schedule.every(15).minutes.do(run)

#job()
#job2()

while True:

	searchterm = input('Enter command: ')
	if searchterm is 's':
		run()
	elif searchterm is 'h':
		hsub()
	elif searchterm is 'r':
		print('Running')
		run()
		while True:
			schedule.run_pending()
			time.sleep(1)		
	elif searchterm:
		searchfor(searchterm)
	else:
		print('invalid')
    

