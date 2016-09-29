class Show:
    title = ''
    episode_count = 0
    source = ''
    episode_list = set()
    watched_list = set()

    def __init__(self, title, episode_count, source):
        Show.title = title
        Show.episode_count = episode_count
        Show.source = source
        for i in range(1, Show.episode_count):
            name = Show.source + ' ' + Show.title + ' ' + str(i)
            Show.episode_list.add(name)

    def print(self):
        for name in Show.episode_list:
            print(name)


temp = Show('test1', 13, 'asrqw')
temp.print()
