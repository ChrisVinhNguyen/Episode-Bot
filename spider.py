from urllib.request import urlopen
from link_finder import LinkFinder
from misc import *

class Spider:

    #class variables
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''

    