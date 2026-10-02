'''
    设置代理  --proxyserver
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_proxy():
    options = Options()
    # 设置代理
    options.add_argument('--proxyserver=http://127.0.0.1:7890')
    driver = webdriver.Chrome(options=options)

    driver.get('http://localhost:8000/tool/request_content')
    proxy = driver.find_element(By.XPATH,'//div[@class="info-card"][1]/div[@class="data-row"][2]/div[@class="data-value"]')
    print(proxy.text)
    driver.quit()


if __name__ == '__main__':
    test_proxy()