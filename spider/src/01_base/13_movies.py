r'''
    搜索电影页面的：
        1、名称
        2、类型
        3、演员
        4、简介

        以下 xpath 写得复杂些主要是为了复习使用，增加练习。可以使用更简单的 xpath 来获取数据。
'''

import requests
import re
import json
from lxml import etree

def get_signal_movie_info(movie_id: int, movie: dict = None):
    # 这个页面是一个电影的详细信息页面
    url = f'http://58.87.96.193:8000/playground/movies/{movie_id}'
    resp = requests.get(url)

    e = etree.HTML(resp.text)

    # 1、电影头部信息通用部分
    movie_info = e.xpath('//div[@class="movie-info"]')

    movie_name = movie_info[0].xpath('./h1/text()')
    # print(f'电影名称：{movie_name[0]}')

    movie_type = movie_info[0].xpath('./div[@class="movie-meta"]/div[@class="meta-item"]/i[@class="fas fa-film"]/../span/text()')
    # print(f'电影类型：{movie_type[0]}')

    # 2、电影演员信息
    move_content = e.xpath('//div[@class="movie-content"]/div[@class="content-sections"]')

    move_intro = move_content[0].xpath(r'./div[@id="intro"]/div/p/text()')
    # print(f'电影简介：{move_intro[0]}')

    movie_actors = move_content[0].xpath(r'./div[@id="actors"]/div/div[@class="actors-full-grid"]/div/div[@class="actor-info"]/div[@class="actor-name"]/text()')
    # print(f'电影演员：{movie_actors}')

    # print('-----------------------------------------------------------------------------------')

    if movie is not None:
        filter = lambda x: x[0] if len(x) > 0 else ''
        movie['name'] = filter(movie_name)
        movie['type'] = filter(movie_type)
        movie['intro'] = filter(move_intro)
        movie['actors'] = movie_actors


def get_page_movie_info(move_page):
    url = f'http://58.87.96.193:8000/playground/7?page={move_page}'
    resp = requests.get(url)

    e = etree.HTML(resp.text)

    # 处理电影列表，获取 movie id
    # 通过正则获取所有电影的 id
    movie_ids = re.findall(r'<div class="movie-item" data-movie-id="(\d+)"', resp.text)
    # print(f'电影 id 列表：{movie_ids}')

    # 调用 get_signal_movie_info 获取每个电影的详细信息，转为 json 写入文件
    movies: list = []
    movie: dict = {}
    for movie_id in movie_ids:
        get_signal_movie_info(movie_id, movie)
        movies.append(movie)
        movie = {}

    json.dump(movies, open(f'src\\spider\\movies\\movie_page_{move_page}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=4)


def get_all_pages_movie_info():
    # 先获取所有的页编号，然后调用 get_page_movie_info 获取每页的电影信息
    # 在页面上的分页处有 -> 共 210 条记录，42 页
    # 方法一：每个电影的id就是 1-210，直接循环获取每个电影的详细信息
    # 方法二：获取每页的电影列表，获取每页的电影id，然后调用 get_signal_movie_info 获取每个电影的详细信息

    url = 'http://58.87.96.193:8000/playground/7'
    resp = requests.get(url)

    e = etree.HTML(resp.text)

    pages = e.xpath(r'//span[@class="page-info"]/text()')

    pages = re.search(r'共 (\d+) 条记录，(\d+) 页', pages[0]).groups()
    print(pages)
    # print(f'记录数：{ids}，页数：{pages}')

    # 遍历所有页，然后获取每页的电影信息
    # for page in range(1, int(pages) + 1):
    #     get_page_movie_info(page)



if __name__ == '__main__':
    # get_signal_movie_info(2)

    # get_page_movie_info(1)

    get_all_pages_movie_info()