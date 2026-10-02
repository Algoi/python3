'''
    拖拽元素
'''
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_move_elem():
    chrome = webdriver.Chrome()
    chrome.get('http://58.87.96.193:8000/playground/14')

    # 获取拖拽元素
    draggable1 = chrome.find_element(by=By.ID, value='draggable')
    draggable2 = chrome.find_element(by=By.ID, value='draggable2')
    draggable3 = chrome.find_element(by=By.ID, value='draggable3')

    # 拖拽元素 - 一步到位
    # drag_and_drop 拖拽元素到指定的元素上，将 draggable1 拖拽到 draggable2 上
    action = webdriver.ActionChains(chrome).drag_and_drop(draggable1, draggable2).perform()

    # 拖拽元素 - 模拟手动拖拽
    # 将 draggable3 拖拽到右下角 100px 的位置
    for i in range(10):
        webdriver.ActionChains(chrome).drag_and_drop_by_offset(draggable3, 10, 10).perform()
        sleep(0.5)

    chrome.quit()


if __name__ == '__main__':
    test_move_elem()