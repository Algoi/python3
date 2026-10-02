'''
    弹窗
        在网页中，弹窗是一种常见的交互方式，通常用于显示重要信息或提示用户进行操作。
        常见三种：
            1、在浏览器顶部，只有确定和取消按钮，没有 ❌ 关闭按钮。这种通常是浏览器自带的弹窗功能
                这种可以直接 switch_to.alert 直接定位到这个弹窗
                    switch_to 焦点集中到页面上的一个警告（提示）
                    accept() 确认弹出窗
                    dismiss() 取消弹出窗
            2、一个隐藏的 div 标签，只有在某个事件触发才会出现
            3、通知，一般不需要处理，会自己消失
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_alert():
    chrome = webdriver.Chrome()
    chrome.get('http://58.87.96.193:8000/playground/13')
    sleep(3)

    # 处理弹窗
    alert = chrome.switch_to.alert
    # 获取弹窗的内容
    print(f'弹窗的内容是：{alert.text}')
    alert.accept() # 点击确定按钮

    # 关闭浏览器
    chrome.quit()


def test_alert2():
    chrome = webdriver.Chrome()
    chrome.get('http://58.87.96.193:8000/playground/13')
    sleep(3)

    # 处理弹窗
    alert = chrome.switch_to.alert
    # 获取弹窗的内容
    print(f'弹窗的内容是：{alert.text}')
    alert.accept() # 点击确定按钮


    # 获取网页中的会弹出弹窗的按钮
    btns = chrome.find_elements(by=By.CLASS_NAME, value='popup-btn')

    # 点击第二个按钮
    btns[1].click()
    confirm = chrome.switch_to.alert
    print(f'弹窗的内容是：{confirm.text}')
    confirm.dismiss() # 点击取消按钮

    # 点击第三个按钮，弹出输入框
    btns[2].click()
    prompt = chrome.switch_to.alert
    print(f'弹窗的内容是：{prompt.text}')
    prompt.send_keys('hello') # 在弹窗中输入内容
    prompt.accept() # 点击确定按钮

    # 点击第四个按钮，弹出自定义模态框（div 标签），这种弹窗不属于浏览器自带的弹窗，无法通过 switch_to.alert 来处理
    btns[3].click()
    # 获取模态框确认按钮
    btn = chrome.find_element(by=By.XPATH, value='//*[@id="customModal"]/div/button[2]')
    print(f'模态框的确认按钮文本是：{btn.text}')
    btn.click() # 点击模态框的确认按钮

    # 点击第六个按钮 逐个弹出多个弹窗
    btns[5].click()
    # 接收第一个弹窗
    chrome.switch_to.alert.accept()
    # 接收第二个弹窗
    chrome.switch_to.alert.accept()
    # 在第三个弹窗中输入内容
    chrome.switch_to.alert.send_keys('hello')
    # 接收第三个弹窗
    chrome.switch_to.alert.accept()


    # 关闭浏览器
    chrome.quit()


if __name__ == '__main__':
    # test_alert()

    test_alert2()