from urllib.request import urlopen

# urllib库是 Python 内置的标准库之一，主要用于处理 URL 相关的操作，如发送 HTTP 请求、获取网页内容等。

# 使用 urllib.request 模块中的 urlopen() 方法发送 HTTP 请求
# 参数为访问的网址，返回一个 HTTPResponse 对象
resp = urlopen("http://www.baidu.com")

# read() 读取服务器返回的网页内容，返回 bytes 类型数据
# decode("utf-8") 将 bytes 按 UTF-8 编码转换为 Python 字符串(str)
# 最后打印网页源码内容
print(resp.read().decode("utf-8"))