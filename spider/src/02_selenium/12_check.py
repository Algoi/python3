'''
    防检测设置
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_check():
    # 创建参数对象
    options = Options()
    # 禁用自动化控制检测
    options.add_argument('--disable-blinkfeatures=AutomationControlled')
    # 禁用网页安全策略
    options.add_argument('--disable-websecurity')
    # 排除自动化开关
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # 禁用自动化扩展
    options.add_experimental_option('useAutomationExtension', False)
    # 创建一个浏览器
    # driver  = webdriver.Chrome()
    driver = webdriver.Chrome(options=options)

    # 和 --disable-blinkfeatures=AutomationControlled 一样的效果
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": "Object.defineProperty(navigator, 'webdriver', {get: () => false})"
    })

    # 访问页面
    driver.get('http://58.87.96.193:8000/playground/17')
    # 获取有没有自动化
    print(driver.execute_script("return window.navigator.webdriver"))

    sleep(5)
    driver.quit()

if __name__ == '__main__':
    test_check()