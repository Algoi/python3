'''
    响应数据格式

    在爬虫开发中，响应数据格式直接决定了后续的解析策略和数据提取方式。
    判断格式的最核心依据是 HTTP 响应头中的 Content-Type 字段。

    Content-Type:
        text/html: HTML 网页
        application/json: JSON 数据
        text/plain: 纯文本
        application/xml: XML 数据

        # 二进制数据格式
        image/png、image/jpeg、image/gif 等：图片数据
        audio/mpeg、audio/wav 等: 音频数据
        video/mp4、video/webm 等: 视频数据
        application/octet-stream: 二进制流数据（如文件下载）

        multipart/form-data: 表单数据（如文件上传）

    Content-Encoding:
        gzip: 响应内容经过 gzip 压缩，需要解压才能获取原始
'''

import requests

resp = requests.get('https://www.baidu.com')

print(resp.headers.get('Content-Type')) # 获取响应头中的 Content-Type 值
print(resp.headers.get('Content-Encoding')) # 获取响应头中的 Content-Encoding 值
print(resp.text) # 获取响应内容，返回字符串类型，requests 会根据响应头中的 Content-Encoding 自动解压 gzip 压缩的内容
print(resp.headers) # 获取响应头信息，返回字典类型


def get_pic():
    url = 'https://pixnio.com/free-images/2026/07/19/2026-07-19-15-14-05-576x434.jpg'
    resp = requests.get(url, headers={'Referer': 'https://pixnio.com/zh/',
                                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36'})
    # print(resp.content)

    '''
        {'Content-Type': 'image/jpeg', 'Accept-Ranges': 'bytes', 'Content-Length': '88572''}
    '''
    print('pic', resp.headers)
    with open('src\\spider\\pic.jpg', 'wb') as f:
        f.write(resp.content) # 写入二进制数据到文件中


if __name__ == '__main__':
     get_pic()