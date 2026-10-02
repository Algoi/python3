r'''
    selenium 等待元素
        网速慢、AJAX请求数据、调试

    selenium 提供了三种等待方式：
        1、强制等待：time.sleep(秒数)
        2、隐式等待：driver.implicitly_wait(秒数)
            作用：在查找元素时，如果元素没有立即出现，就等待一段时间
            适用场景：元素在一定时间内会出现
            注意：只能等待元素出现在 DOM 中
        3、显式等待：WebDriverWait(driver, timeout, poll_frequency).until
            常见的等待条件
                EC.presence_of_element_located() 元素存在
                EC.visibility_of_element_located() 元素可见
                EC.element_to_be_clickable() 元素可点击
                EC.presence_of_all_elements_located() 所有元素存在
            作用：等待指定条件成立，专门用于对指定一个元素等待，不用等待全部元素加载完
            适用场景：元素出现的时间不确定，需要等待特定条件满足
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def test_force_wait():
    chrome = webdriver.Chrome()
    chrome.get('http://58.87.96.193:8000/playground/16')

    # 定位元素
    btn = chrome.find_element(By.ID, 'loadContentBtn')
    sleep(1)  # 强制等待，等待按钮加载出来
    # 点击按钮
    btn.click()
    # 获取延迟加载的数据
    div = chrome.find_element(By.ID, 'delayedContent')
    sleep(3) # 强制等待，等待数据加载出来
    # 打印数据
    print(div.text)

    chrome.quit()


def test_implicit_wait():
    chrome = webdriver.Chrome()

    '''
        这个案例中，隐式等待不好用，因为隐式等待只能等待元素出现在 DOM 中，而这个案例中，元素已经出现在 DOM 中了，只是没有数据，所以隐式等待无法解决问题
    '''

    chrome.implicitly_wait(5)  # 隐式等待，等待元素加载出来，最长等待5秒

    chrome.get('http://58.87.96.193:8000/playground/16')

    # 定位元素
    btn = chrome.find_element(By.ID, 'loadContentBtn')
    # 点击按钮
    btn.click()
    # 获取延迟加载的数据
    div = chrome.find_element(By.ID, 'delayedContent')
    # 打印数据
    print(div.text)

    chrome.quit()


def test_implicit_wait2():
    chrome = webdriver.Chrome()

    chrome.implicitly_wait(5)  # 隐式等待，等待元素加载出来，最长等待5秒

    chrome.get('http://58.87.96.193:8000/playground/16')

    # 定位元素
    btn = chrome.find_element(By.ID, 'gridBtn')
    # 点击按钮
    btn.click()
    # 获取延迟加载的数据，这里的数据才是点击按钮之后动态显示的（通过js动态添加的）
    div = chrome.find_element(By.XPATH, '//*[@id="elementGrid"]/div[3]')  # 获取第一个可见的元素, 这里不要用 last() 否则会认为第一个加载出来的就是最后一个
    # 打印数据，但是仍然可能打印不出数据
    # 原因：确实等了，但是没有等完，需要配合 sleep 再等一会儿
    sleep(0.2)
    print(div.text)

    chrome.quit()




if __name__ == '__main__':
    # test_force_wait()

    # test_implicit_wait()
    test_implicit_wait2()