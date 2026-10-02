r'''
    1、最大化窗口
        调用启动的浏览器不是全屏的。
    2、设置高与宽
        最大化可能还是不够灵活，随意设置宽和高更灵活。
    3、浏览器前进、后退
        浏览器有前进和后退按钮。
'''

from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
url = 'https://www.baidu.com'
browser.get(url)
# sleep(10)

browser.maximize_window()  # 最大化窗口
browser.save_screenshot('src\\spider\\index.png') # 保存截图，如果窗口没有全屏，只会截部分
sleep(2)
browser.set_window_position(100, 200)  # 设置窗口位置
sleep(2)
browser.set_window_size(800, 600)  # 设置窗口大小
sleep(2)

next_url = "https://www.sogou.com"
browser.get(next_url)


browser.back() # 浏览器后退，返回 baidu

browser.forward() # 浏览器前进，返回 sogou

# sleep(10)
browser.quit()

