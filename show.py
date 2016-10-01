from downloader import *

class Show:

    def __init__(self, title, episode_count, source):
        Show.title = title
        Show.episode_count = episode_count
        Show.source = source
        Show.episode_list = []
        Show.watched_list = []

        for i in range(1, Show.episode_count + 1):
            if Show.source == 'HorribleSubs':
                if i < 10:
                    name = '[' + Show.source + '] ' + Show.title + ' - 0' + str(i) +' [1080p]'
                    Show.episode_list.append(name)
                else:
                    name = '[' + Show.source + '] ' + Show.title + ' - ' + str(i) + ' [1080p]'
                    Show.episode_list.append(name)

    def print_info(self):
        for name in Show.episode_list:
            print(name)

    def find_episodes(self,html):
        for item in Show.episode_list:
            name = item + '.mkv'
            link = find_episode(html,name)
            if link != 'error, not found':
                file_name = 'downloads/' + name + '.torrent'
                print('downloading file ----------> ' + name)
                download_episode(link,file_name)






