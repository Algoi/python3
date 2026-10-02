'''
    执行 JavaScript 代码
        有时候我们需要控制页面滚动条上的滚动条，但滚动条并非页面上的元素，这个时候就需要借助js是来进行操作
        一般用到操作滚动条的会两个场景：
            1、要操作的页面元素不在当前页面范围，无法进行操作，需要拖动滚动条
            2、注册时的法律条文需要阅读，判断用户是否阅读的标准是：滚动条是否拉到最下方

    selenium 提供了 execute_script(script, *args) 方法来执行 JavaScript 代码
        // 拉动滚动条，可以先到浏览器控制台中测试，可能适配的浏览器不一样
        document.元素.scrollTop=高度
        document.元素.scrollTo(宽度, 高度)
        window.scrollTo(宽度, 高度)

        // 获取页面高度
        document.body.scrollHeight
        // 获取元素高度
        document.getElementById('scrollContent').scrollHeight
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

def test_js():
    chrome = webdriver.Chrome()
    chrome.get('http://58.87.96.193:8000/playground/15')

    # 拉动整个页面的滚动条
    js1 = 'document.documentElement.scrollTop=100'

    # 拉动指定元素的滚动条
    js2 = 'document.getElementById("scrollContent").scrollTop=100'

    chrome.execute_script(js1)

    chrome.execute_script(js2)

    chrome.quit()


if __name__ == '__main__':
    test_js()