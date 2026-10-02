'''
    设置无头浏览器，不显示界面。
        可以提升效率
        对于无界面的 linux 等场景适用
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_headless():
    options = Options()
    options.add_argument('--headless')  # 设置无头浏览器
    # options.add_argument('--headless=new') # chrome 109 及其以上版本

    chrome = webdriver.Chrome(options=options)
    chrome.get('http://58.87.96.193:8000/playground/17')
    div = chrome.find_element(By.TAG_NAME, 'h3')
    print(div.text)

    chrome.quit()


if __name__ == '__main__':
    test_headless()