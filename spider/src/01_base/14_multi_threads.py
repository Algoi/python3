r'''
    单线程爬虫问题：
        1、爬虫多为IO密集型程序，而处理IO速度并不快
        2、如果IO卡顿，直接影响爬虫速度

    可以考虑使用多线程、多进程和协程解决这个问题

    核心思路：
        爬虫使用多线程来处理网络请求，使用线程来处理URL队列中的url，
        然后将url返回的结果保存在另一个队列中，其它线程在读取这个队列中的数据，然后写到文件中。
'''

'''
    1、使用多线程实现并发爬取
        from queue import Queue 借助 queue 模块实现数据同步
        Python的Queue模块中提供了同步的、线程安全的队列类，
        包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。
        这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。

        常用操作如下：
        Queue.qsize() 返回队列的大小
        Queue.empty() 如果队列为空，返回True,反之False
        Queue.full() 如果队列满了，返回True,反之False
        Queue.full 与 maxsize 大小对应
        Queue.get([block[, timeout]])获取队列，timeout等待时间
        Queue.get_nowait() 相当Queue.get(False)
        Queue.put(item) 写入队列，timeout等待时间
        Queue.put_nowait(item) 相当Queue.put(item, False)
        Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
        Queue.join() 实际上意味着等到队列为空，再执行别的操作
'''
from queue import Queue
from threading import Thread
import threading
import json
import requests

def generate_url(pages: list):
    '''
        生成需要爬取的所有网页的 url，这里的案例是爬取不同 page 页面的电影信息，返回 json数据
        pages: 要爬取的页的编号
    '''
    url_queue = Queue()
    for page in pages:
        url_queue.put(f'http://58.87.96.193:8000/api/movies?page={page}&movie_type=&movie_time=')

    return url_queue

def spider_thread_func(urls: Queue, out: Queue):
    '''
        爬虫线程函数，获取 url 队列中的 url，然后爬取数据
    '''
    while not urls.empty():
        url = urls.get(timeout=1) # 获取 url 队列中的 url，timeout 超时等待时间
        resp = requests.get(url).json()

        out.put(resp) # 将爬取结果放入输出队列中

        print(f'Thread {threading.current_thread().name} 爬取 {url} 成功，返回数据：{len(resp.get("items"))}')

        urls.task_done() # 标记 url 队列中的任务完成

class SpiderThread(Thread):
    '''
        爬虫线程类，继承自 Thread 类
    '''
    def __init__(self, out_queue: Queue):
        super().__init__()
        self.out_queue = out_queue

    def run(self):
        while not self.out_queue.empty():
            result = self.out_queue.get()
            with open(f'src\\spider\\movies\\movie_page_{result.get("page")}.json', 'w', encoding='utf-8') as f:
                json.dump(result.get("items"), f, ensure_ascii=False, indent=4) # 将结果 json 写入文件


def multi_thread_spider():
    # 1、生成要爬取的 url 队列
    url_queue = generate_url([i for i in range(1, 12)])

    # 2、创建线程并启动
    out_queue = Queue() # 用于保存爬取结果的队列
    THREAD_NUM = 11
    for i in range(THREAD_NUM):
        t = Thread(target=spider_thread_func, args=(url_queue, out_queue))
        t.start()

    url_queue.join() # 等待所有 url 爬取完成

    # 3、处理所有结果数据
    for i in range(THREAD_NUM):
        t = SpiderThread(out_queue)
        t.start()


import time
if __name__ == '__main__':
    now = time.time()
    multi_thread_spider()
    print(f'爬取完成，耗时：{time.time() - now} 秒')

