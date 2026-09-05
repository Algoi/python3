'''
    保存和使用 cookie
        1、直接从浏览器拷贝
        2、保存到本地文件中
        3、使用 session 对象，该对象自动保存这 cookie 信息
'''

import requests

def login():
    url = 'http://58.87.96.193:8000/playground/login'
    info = {
        'uname':'admin',
        'password':'123456'
    }

    sess = requests.Session()
    resp = sess.post(url, data=info)

    '''
        cookies 保存到文件中，也可以直接返回给后续代码使用
    '''
    with open('src\\spider\\cookies.txt', 'w') as f:
        for key, val in sess.cookies.items():
            f.write(f'{key}:{val}')

    print(resp.status_code)


def use_cookies():
    url = 'http://58.87.96.193:8000/playground/user_info'
    cookies = {}
    with open("src\\spider\\cookies.txt", 'r') as f:
        for line in f.readlines():
            key, val = line.strip().split(':')
            cookies[key] = val

    # resp = requests.get(url, cookies=cookies) # 通过 cookies 参数传递 cookie 字典
    resp = requests.get(url, headers={"Cookie": "; ".join([f"{key}={val}" for key, val in cookies.items()])})
    print(resp.status_code)


def get_user_info():
    url = 'http://58.87.96.193:8000/playground/login'
    form_data ={
        'uname':'admin',
        'password':'123456'
    }

    # 获取可以保存cookie的请求对象
    sess = requests.Session()
    login_resp  = sess.post(url,data=form_data)
    # print(login_resp.text)

    url = 'http://58.87.96.193:8000/playground/user_info'
    info_resp = sess.get(url)
    print(info_resp.text)


if __name__ == '__main__':
    # login()
    # use_cookies()

    get_user_info()