r'''
    selenium 定位下拉框和选择
        <select>
            <option/>
            <option/>
            <option/>
            ...
        </select>

        可以通过 XPath 或其他方式定位到具体的 option 元素并进行选择。
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_select():
    # 打开浏览器
    browser = webdriver.Chrome()

    # 访问链接
    browser.get('http://58.87.96.193:8000/playground/11')

    # 获取下拉框元素及其定位
    # select_elem = browser.find_element(by=By.ID, value='MovieTime') # 整个下拉框元素
    op1 = browser.find_element(by=By.XPATH, value='//*[@id="MovieTime"]/option[7]') # 获取第 7 个 option 元素
    op1.click() # 选择第 7 个 option

    op2 = browser.find_element(by=By.XPATH, value='//*[@id="SeatType"]/option[2]')
    op2.click() # 选择第 2 个 option

    sleep(3)
    browser.quit() # 关闭浏览器


def test_dropdown():
    '''
        有的时候，网页中的下拉框并不是 <select> 标签，而是通过 <div>、<ul>、<li> 等标签实现的，这种下拉框的选择方式和普通的点击操作类似。
        这种需要先点击，然后才会弹出选项，无法直接通过定位的方式进行选择
    '''
    chrome = webdriver.Chrome()
    chrome.get('http://58.87.96.193:8000/playground/10')
    sleep(2)

    '''
        方法一：先点击下拉框按钮，然后再选择选项
    '''
    # 获取第一个菜单按钮并点击，它才能弹出选项并选择
    dropdown1 = chrome.find_element(by=By.ID, value='dropdownMenu1')
    dropdown1.click() # 点击第一个菜单按钮，弹出选项
    sleep(2)
    print(f'点击了{dropdown1.text}按钮，弹出选项')
    # 选择弹出的菜单选项
    op1 = chrome.find_element(by=By.ID, value='action1') # 选择第一个
    op1.click() # 点击第一个选项
    print(f'选择了 --{op1.text}-- 选项')


    '''
        方法二：建立一个动作，模拟鼠标行为
    '''
    # 先定位到菜单按钮
    dropdown2 = chrome.find_element(by=By.ID, value='dropdownMenu2')
    webdriver.ActionChains(chrome).move_to_element(dropdown2).perform() # 鼠标移动到菜单按钮上并点击
    dropdown2.click() # 点击第二个菜单按钮，弹出选项
    print(f'点击了{dropdown2.text}按钮，弹出选项')
    sleep(2)

    op2 = chrome.find_element(by=By.ID, value='iconAction1') # 选择第一个选项
    op2.click() # 点击第一个选项
    print(f'选择了 --{op2.text}-- 选项')

    # 关闭
    sleep(3)
    chrome.quit()

if __name__ == '__main__':
    # test_select()

    test_dropdown()