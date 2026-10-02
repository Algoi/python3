# selenium 4.6.0 以前需要手动下载对应浏览器的驱动
# current selenium == 4.50.0

from selenium import webdriver
from time import sleep

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 访问页面，打开一个浏览器页面
driver.get("http://www.baidu.com")
sleep(2) # 页面响应比较慢，可以睡眠几秒

# 获取页面的内容，整个 html
print(driver.page_source)

# 关闭浏览器
driver.quit()