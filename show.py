from downloader import *

class Show:

    def __init__(self, title, episode_count, source , season,quality,file_name):
        Show.title = title
        Show.episode_count = episode_count
        Show.source = source
        Show.season = season
        Show.quality = quality
        Show.file_name = file_name
        Show.episode_list = []
        Show.watched_list = []

        for i in range(1, Show.episode_count + 1):
            if Show.source == 'HorribleSubs':
                if i < 10:
                    name = Show.title + ' - 0' + str(i)
                    Show.episode_list.append(name)
                else:
                    name = Show.title + ' - ' + str(i)
                    Show.episode_list.append(name)

    def print_info(self):
        for name in Show.episode_list:
            print(name)

    def find_episodes(self,html):
        for item in Show.episode_list:
            name = item
            episode_number = ' ' +name[-2:] + ' '
            link = find_episode(html,Show.title,Show.source,Show.quality,episode_number)
            if link != 'error, not found':
                file_name = 'downloads/' + name + ' S' + str(Show.season) + '.torrent'
                if os.path.isfile(file_name):
                    print('Already downloaded')
                    return
                print('downloading file ----------> ' + name)
                download_episode(link,file_name)
                download_torrent(file_name,Show.title,Show.season,Show.file_name)






