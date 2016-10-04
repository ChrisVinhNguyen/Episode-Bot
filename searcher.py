import yaml
from show import Show

def search(path,html):

    stream = open(path, "r")
    docs = yaml.load_all(stream)
    for doc in docs:
        title = 'placeholder_title'
        episode_count = 0
        source = ''
        season = 1
        quality = ''
        file_name = ''
        for k, v in doc.items():
            if k == 'title':
                title = v
                file_name = v
            if k == 'episode_count':
                episode_count = v
            if k == 'source':
                source = v
            if k == 'season':
                season = v
            if k == 'quality':
                quality = v
            if k == 'file_name':
                file_name = v
            temp = Show(title,episode_count,source,season,quality,file_name)
        if episode_count != 0:
            #temp.print_info()
            print('Searching for....' + temp.title)
            temp.find_episodes(html)




