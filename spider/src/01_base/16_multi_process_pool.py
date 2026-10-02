from multiprocessing import Pool, Manager
import re
import requests


def generate_url(pages, url_queue):
    """
    生成待爬取的 URL，放入进程安全队列。
    """
    for page in pages:
        url_queue.put(
            f'http://58.87.96.193:8000/api/movies?page={page}&movie_type=&movie_time='
        )


def spider(url_queue):
    while True:
        try:
            url = url_queue.get_nowait()
        except Exception:
            break

        resp = requests.get(url)

        page = re.search(r"page=(\d+)", url).group(1)

        data = resp.json()

        print(f"获取 page={page} 的数据: {data}")


if __name__ == '__main__':

    # Manager 创建的 Queue 可以作为 Pool 任务参数传递
    with Manager() as manager:

        urls = manager.Queue()

        generate_url(range(1, 11), urls)

        with Pool(3) as pool:

            results = []

            for _ in range(3):
                result = pool.apply_async(
                    func=spider,
                    args=(urls,)
                )
                results.append(result)

            # 主动获取结果，可以发现子进程异常
            for result in results:
                result.get()