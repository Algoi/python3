'''
    层级定位
        iframe 引入子页面，在获取子页面元素时，需要先切换到子页面，再获取元素
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def select_frame():
    chrome = webdriver.Chrome()
    chrome.get('http://58.87.96.193:8000/playground/12')
    sleep(2)

    # 切换 iframe
    chrome.switch_to.frame('f1') # 通过 id 切换到对应的 iframe
    # 定位元素
    div = chrome.find_element(by=By.CLASS_NAME, value='stat-number') # 通过 class 定位元素
    print(f'iframe 中的一个div元素内容是：{div.text}')

    # 关闭浏览器
    chrome.quit()


if __name__ == '__main__':
    select_frame()