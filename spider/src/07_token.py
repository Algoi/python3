'''
    Token的基本概念是一种常见的HTTP认证方案，它使用安全令牌来进行身份验证。
    当服务器响应登录请求时，通常会生成这个token。

    Token的使用场景：
        API接口认证
        需要登录的网站爬取
        受保护资源的访问
    Token有效期：很多token都有过期时间，需要及时更新
'''

import requests

def get_user_info():
    url = 'http://58.87.96.193:8000/playground/login2'
    json_data = {
        'uname':'admin',
        'password':'123456'
    }

    resp = requests.post(url, json=json_data)
    '''
        {"user":{"uname":"sxt","password":"123456","email":"admin@example.com","role":"管理员","VIP":"黄金会员"},
         "access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc4ODUzMjI0Mn0.7mmorA3tBrPfariCmaO6dwODP1I9pmakbM-46qCOeFs"}
    '''
    print(resp.status_code, resp.text)

    # 获取 access_token
    access_token = resp.json().get('access_token')
    print("Access Token:", access_token)

    user_info_url = 'http://58.87.96.193:8000/playground/user_info2'
    resp = requests.get(user_info_url, headers={"Authorization": f"Bearer {access_token}"})
    print("User Info:", resp.status_code, resp.text)

if __name__ == '__main__':
    get_user_info()