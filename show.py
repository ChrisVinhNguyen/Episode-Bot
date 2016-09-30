class Show:

    #title = ''
    #episode_count = 0
    #source = ''
    #episode_list = set()
    #watched_list = set()

    def __init__(self, title, episode_count, source):
        Show.title = title
        Show.episode_count = episode_count
        Show.source = source
        Show.episode_list = set()
        Show.watched_list = set()
        
        for i in range(1, Show.episode_count + 1):
            name = Show.source + ' ' + Show.title + ' ' + str(i)
            Show.episode_list.add(name)

    def print_info(self):
        for name in Show.episode_list:
            print(name)



