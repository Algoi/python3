'''
    requests 是 Python 中最常用的 HTTP 请求库，用于向服务器发送 HTTP 请求（GET、POST、PUT、DELETE 等），获取网页、调用 REST API、上传下载文件等。
    相比 Python 内置的 urllib，requests 的 API 更简单、更符合人的使用习惯。

    安装 pip install requests
    官方文档：https://requests.readthedocs.io/en/latest/
'''

import requests

'''
    1、requests 库的发送请求常用方法：
        requests.get()：发送 GET 请求 -> def get(url: _t.UriType, params: _t.ParamsType = None, **kwargs: Unpack[_t.GetKwargs]) -> Response:
        requests.post()：发送 POST 请求 -> def post(url: _t.UriType, data: _t.DataType = None, json: _t.JsonType = None, **kwargs: Unpack[_t.PostKwargs]) -> Response:
        requests.put()：发送 PUT 请求
        requests.delete()：发送 DELETE 请求
        requests.head()：发送 HEAD 请求
        requests.options()：发送 OPTIONS 请求
'''
def send_requests():
    resp = requests.get("http://www.baidu.com")
    resp = requests.post("http://www.baidu.com")
    resp = requests.put("http://www.baidu.com")
    resp = requests.delete("http://www.baidu.com")
    resp = requests.head("http://www.baidu.com")
    resp = requests.options("http://www.baidu.com")


'''
    2、获取响应信息
'''
def get_resp_info():
    resp = requests.get('https://requests.readthedocs.io/en/latest/user/quickstart', headers={"test": "my_test"})

    print(resp.text) # 获取响应内容，返回字符串类型
    print(resp.content.decode('utf-8')) # 获取响应内容，返回字节类型，需要解码才能看懂
    # print(resp.json()) # 获取响应的 JSON 数据，返回字典类型，如果响应内容不是 JSON 格式，会抛出异常(比如返回 html，就不能用 json 转)

    print(resp.encoding) # 获取响应内容的编码方式，比如 utf-8
    print(resp.status_code) # 获取响应状态码，比如 200、404、500 等
    print(resp.headers) # 获取响应头信息，返回字典类型
    print(resp.request.headers) # 获取请求头信息，返回字典类型，比如 headers 中的 test 请求头就在其中
    print(resp.url) # 获取请求的地址
    print(resp.cookies) # 获取响应的 Cookie 信息，返回 RequestsCookieJar 类型

    print(resp.history) # 获取重定向历史，返回一个 Response 对象的列表，如果没有重定向，则返回空列表


'''
    3、post 请求的请求体数据
        3.1 form 表单数据：data 参数，字典类型
        3.2 json 数据：json 参数，字典类型
'''
def form_data():
    url='http://58.87.96.193:8000/playground/add_role1'
    form_data = {'name':'孙权', 'book':'三国'}
    # 使用 post 请求发送表单数据，data 参数传入字典类型的 form_data
    resp = requests.post(url, data=form_data)
    print(resp.text)

def json_data():
    url ="http://58.87.96.193:8000/playground/add_role2"
    json_data = {'name':'典韦','book':'三国'}
    # 使用 post 请求发送 json 数据，json 参数传入字典类型的 json_data
    resp = requests.post(url,json=json_data)
    print(resp.text)

if __name__ == '__main__':
    # form_data()
    json_data()