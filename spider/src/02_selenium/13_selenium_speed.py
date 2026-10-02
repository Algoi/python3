'''
    selenium 提升爬取效率
        1、解析方面
            selenium本身提取数据，会比使用XPath、BS4、re这种提取方式要慢。因为每一个selenium的操作，都需要和浏览器通信

            # 先用Selenium获取动态内容
            driver.get(url)

            # 然后用XPath解析，这样更快
            e = etree.HTML(driver.page_source)
            data = e.xpath('//div')

        2、参数设置
            无头浏览器等

        3、并发编程
            多进程
            协程:
                Playwright
                Pyppeteer
                aiohttp

'''

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from lxml import etree


class Parser_Method:
    '''
        比较 selenium 的解析方式和 xpath 解析方式效率提升
    '''
    @staticmethod
    def test_speed_parse_html_with_selenium():
        chrome = webdriver.Chrome()
        chrome.get("http://58.87.96.193:8000/playground/1")

        start = time.time()
        h3 = chrome.find_element(By.TAG_NAME, 'h3')
        print(h3.text)
        end = time.time()

        print(f'find_element 耗时：{end - start}')


    @staticmethod
    def test_speed_parse_html_with_xpath():
        chrome = webdriver.Chrome()
        chrome.get("http://58.87.96.193:8000/playground/1")

        start = time.time()
        e = etree.HTML(chrome.page_source)
        h3 = e.xpath('//h3')
        print(h3[0].text)
        end = time.time()

        print(f'xpath 耗时：{end - start}')


class Options_Setting:
    '''
        selenium 参数设置提升效率
    '''
    @staticmethod
    def test_speed_with_selenium():
        chrome = webdriver.Chrome()
        chrome.get("http://58.87.96.193:8000/playground/7")

        start = time.time()
        e = etree.HTML(chrome.page_source)
        h3 = e.xpath('//h3//text()')
        for h in h3:
            print(h)

        end = time.time()

        print(f'with header 耗时：{end - start}')

    @staticmethod
    def test_speed_with_options():
        ops = Options()
        ops.add_argument('--headless')  # 设置无头浏览器
        ops.add_argument('--disable-gpu')  # 禁用GPU加速
        ops.add_argument('--disable-extensions')  # 禁用扩展
        ops.add_argument('--disable-images')  # 禁用图片加载
        ops.add_argument('--no-sandbox')  # 禁用沙箱
        ops.add_argument('--disable-javascript')  # 禁用JavaScript

        chrome = webdriver.Chrome(options=ops)
        chrome.get("http://58.87.96.193:8000/playground/7")

        start = time.time()
        e = etree.HTML(chrome.page_source)
        h3 = e.xpath('//h3//text()')
        for h in h3:
            print(h)

        end = time.time()

        print(f'no header 耗时：{end - start}')


if __name__ == '__main__':
    # Parser_Method.test_speed_parse_html_with_selenium()
    # Parser_Method.test_speed_parse_html_with_xpath()

    Options_Setting.test_speed_with_selenium()
    Options_Setting.test_speed_with_options()