"""
ニュース記事の情報をとってくる
"""
import time

import requests


def main():
    time.sleep(1)
    stories = get_top_stories()

    for i in range(len(stories)):
        if i >= 5:
            break
        time.sleep(1)
        story = get_story_by_id(stories[i])
        print(story)


def get_story_by_id(story_id):
    url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
    params = {'print': 'pretty'}
    response = requests.get(url, params)
    story_dict = response.json()
    return {'title': story_dict['title'], 'link': story_dict['url']}


def get_top_stories():
    url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
    params = {'print': 'pretty'}
    response = requests.get(url, params)
    stories = response.json()
    return stories


if __name__ == '__main__':
    main()