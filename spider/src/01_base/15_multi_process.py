r'''
    multiprocessing是python的多进程管理包，和threading.Thread类似
    multiprocessing模块可以让程序员在给定的机器上充分的利用CPU在multiprocessing中，
    通过创建Process对象生成进程，然后调用它的start()方法

'''

from multiprocessing import Process, Manager
import re
import requests


def generate_url(pages: list, urls):
    '''
        生成需要爬取的所有网页的 url，这里的案例是爬取不同 page 页面的电影信息，返回 json数据
        pages: 要爬取的页的编号
    '''
    for page in pages:
        urls.put(f'http://58.87.96.193:8000/api/movies?page={page}&movie_type=&movie_time=')


def spider(url_queue):
    while not url_queue.empty():
        url = url_queue.get()
        resp = requests.get(url)
        page = re.findall(r"page=(\d+)", url)
        data = resp.json()
        print(f"获取 page={page} 的数据{data}")

if __name__ == '__main__':
    urls = Manager().Queue()
    generate_url(range(1, 11), urls)

    all_process = []
    for i in range(3):
        p = Process(target=spider, args=(urls,))
        all_process.append(p)
        p.start()

    [p.join() for p in all_process]
