import yaml
from show import Show

def load_yaml(path):

    list=set()
    title = 'placeholder_title'
    episode_count = 0
    source = 'placeholder_source'

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
            temp = Show(title,episode_count,source)

    return list



