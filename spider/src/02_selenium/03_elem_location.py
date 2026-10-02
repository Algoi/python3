r'''
    selenium 元素定位
        对象的定位是自动化的核心，要操作一个对象，首先应该识别出这个对象

    webdriver 提供了对象定位方法
        find_element(type,value)
        find_elements(type,value)

        利用 By 类来确定哪种选择方式
            from selenium.webdriver.common.by import By
            chrome.find_element(by=By.ID, value='index')
                By 类的一些属性如下
                    ID = "id"
                    NAME = "name"
                    XPATH = "xpath"
                    LINK_TEXT = "link text"
                    PARTIAL_LINK_TEXT = "partial link text"
                    TAG_NAME = "tag name"
                    CLASS_NAME = "class name"
                    CSS_SELECTOR = "css selector"

    操作元素
        定位元素之后，需要对元素进行操作
            click 点击对象，比如 button
            send_keys 在对象上模拟按键输入，比如 input 输入框
            clear 清除对象的内容，比如输入框
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器
browser = webdriver.Chrome()

# 访问链接
browser.get('http://58.87.96.193:8000/playground/4')

# 获取内容, XPATH 直接从浏览器中拷贝即可
p = browser.find_element(by=By.XPATH, value='/html/body/main/div/div/div/div[1]/p')
print(p.text) # 获取 p 标签中文本的内容

# 操作表单中的控件
# 获取用户名输入框
user_input = browser.find_element(by=By.ID, value='name') # 通过 id 定位元素
user_input.send_keys('弗利萨') # 在输入框中输入内容

book_input = browser.find_element(by=By.ID, value='book')
book_input.send_keys('龙珠')

# 获取提交按钮
submit_btn = browser.find_element(by=By.XPATH, value='//*[@id="roleForm"]/button')
submit_btn.click() # 点击提交按钮

# 停止浏览器
browser.quit()