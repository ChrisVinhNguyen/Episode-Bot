import yaml
from show import Show

def search(path,html):

    title = 'placeholder_title'
    episode_count = 0
    source = 'placeholder_source'
    season = 1

    stream = open(path, "r")
    docs = yaml.load_all(stream)
    for doc in docs:
        for k, v in doc.items():
            if k == 'title':
                title = v
            if k == 'episode_count':
                episode_count = v
            if k == 'source':
                source = v
            if k == 'season':
                season = v
            temp = Show(title,episode_count,source,season)
        if episode_count != 0:
            #temp.print_info()
            print('Searching for....' + temp.title)
            temp.find_episodes(html)




