'''
    网络部分信息或APP的信息，若是想获取数据时，需要提前做一些操作，往往是需要登录，或者提前访问过某些页面才可以获取到！！
    其实底层就是在网页里面增加了Cookie信息。
'''

import requests

def login() -> str:
    url = "http://58.87.96.193:8000/playground/login"
    form_data = {
        'uname':'admin',
        'password': '123456'
    }

    '''
        获取 Session() 函数可以获取一个会话对象。
        通过这个会话发送请求，后面可以获取到响应的 Cookie 信息。
    '''
    sess = requests.Session()
    resp = sess.post(url, data=form_data)

    # 比如输出 [('session', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc4ODUyOTU4N30.bvtl5qcB7Ed8c6MkhLXZ5pws7BbAtmBfpA3d8jeKCnY')]
    print(sess.cookies.items()) # 获取响应的 Cookie 信息
    print(resp.status_code)

    return sess.cookies.items()


def get_user1(cookies: list):
    '''
        1、使用 cookies 参数传入 Cookie 信息
    '''
    url = 'http://58.87.96.193:8000/playground/user_info'
    cks = {}
    for i in cookies:
        cks[i[0]] = i[1]

    cks['Max_Age'] = '600'
    cks['Path'] = '/'

    resp = requests.get(url, cookies=cks)
    print(resp.status_code)


def get_user2(cookies: list):
    '''
        2、使用 headers 参数传入 Cookie 信息
    '''
    url = 'http://58.87.96.193:8000/playground/user_info'
    cks = ''
    for i in cookies:
        cks += f"{i[0]}={i[1]}; "

    cks += 'Max_Age=600; Path=/'

    headers = {
        'Cookie': cks
    }

    resp = requests.get(url, headers=headers)
    print(resp.status_code)

if __name__ == '__main__':
    cookies = login()
    get_user1(cookies)
    get_user2(cookies)