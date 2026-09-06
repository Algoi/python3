'''
    1、Beautiful Soup 页面提取数据

        官网 http://beautifulsoup.readthedocs.io/zh_CN/latest/

        Beautiful Soup 是一个用于解析 HTML/XML 的 Python 库，提供简单易用的导航、搜索和修改文档结构功能，常用于爬虫数据提取。
        它会自动处理 Unicode 和 UTF-8 编码，也可以配合 `lxml`、`html5lib` 等解析器使用，在易用性、兼容性和性能之间灵活选择。

        Beautiful Soup 安装
            pip install beautifulsoup4
            pip install bs4

        Beautiful Soup 支持Python标准库中的HTML解析器, 还支持一些第三方的解析器,
        如果不安装它, 则 Python 会使用 Python 默认的解析器, lxml 解析器更加强大，速度更快，推荐安装 lxml
        pip install lxml
'''

from bs4 import BeautifulSoup
import bs4

html = '<h1>Hello</h1>'

bs = BeautifulSoup(html, "lxml") # 指定 lxml 解析器
print(bs) # <html><body><h1>Hello</h1></body></html>


'''
    2、四大对象种类
        Beautiful Soup 将复杂 HTML 文档转换成一个复杂的树形结构，
        每个节点都是 Python 对象，所有对象可以归纳为3种：
            * BeautifulSoup
                文档根节点，这个对象代表了整个被解析的文档。是一个特殊的 Tag 对象，可以看作是文档树的根节点。
                它的 .name 属性通常是 "[document]"
                判断方法：isinstance(node, bs4.BeautifulSoup)
            * Tag
                最为重要的节点类型，对应 html 或 xml 中每一个标签（如 <div>、<a>、<p> 等）都是一个 Tag 对象。
                可以调用 .name 获取标签名，可以向操作字典一样用 .attrs 或者直接 ['属性名'] 获取属性。
                判断方法：isinstance(tag, bs4.element.Tag)
                soup.p 返回的就是一个 Tag 对象
            * NavigableString
                可导航字符串 -- 文本内容
                这是标签内部包含的文本字符串，即标签闭合之间的内容
                本质上就是一个 Unicode 字符串，但增加了与文档数交互（如 .parent 或 .next_sibling 等）的功能。
                判断方法：isinstance(string, bs4.element.NavigableString)
                soup.p.string 返回的就是一个 NavigableString 对象
            * Comment
                注释及其他特殊字符串 -- 隐藏的文本
                HTML 中的注释 <!-- 注释内容 --> 会被解析为 Comment 对象。
                特征：它属于 NavigableString 的子类，但在渲染（即 .prettify()）时不会显示注释符号。
'''

def test_bs4():
    html = '''
    <title>尚学堂</title>
    <div class='info' float='left'>Welcome to Python</div>
    <div class='info' float='right'>
        <span>Good Good Study</span>
        <a href='www.github.cn'></a>
        <strong><!--没用--></strong>
    </div>
    '''
    soup = BeautifulSoup(html, 'lxml')

    # 1、BeautifulSoup 对象
    print(type(soup), isinstance(soup, BeautifulSoup)) # <class 'bs4.BeautifulSoup'> True 根节点
    print(soup.name) # [document]

    # 2、Tag 对象
    # 相同的标签只能获取第一个符合要求的标签
    div = soup.div
    print(type(div), isinstance(div, bs4.element.Tag)) # <class 'bs4.element.Tag'> True 标签节点
    print(div) # <div class="info" float="left">Welcome to Python</div>
    print(div.name) # div

    # 获取 Tag 对象属性
    print(soup.div.attrs) # {'class': ['info'], 'float': 'left'}
    print(soup.div.get('class'), soup.div.get('float')) # ['info'] left
    print(soup.div['class'], soup.div['float']) # ['info'] left

    # 3、NavigableString 对象
    '''
        .string：获取的是当前标签下唯一的文本节点。如果标签内有多个文本块（比如夹杂了子标签），它会返回 None。
        .text（或 .get_text()）：获取的是当前标签下所有后代文本的拼接，无论嵌套多深，永远返回一个字符串。

        .string：是“精挑细选”的，只有一个才给你，多了就返回 None（常用于处理 <title>、<h1> 这种纯标题）。
        .text 是“通吃”的，不管多少个，全给你合并成一个字符串（常用于提取大段正文或所有可见文字）。
    '''
    print(soup.div.string, soup.div.text)
    print(type(soup.div.string), type(soup.div.text)) # <class 'bs4.element.NavigableString'> <class 'str'>
    print(soup.div.string, soup.div.text) # Welcome to Python Welcome to Python
    print(type(soup.strong.string), (soup.strong.text)) # <class 'bs4.element.Comment'> <class 'str'>
    print(soup.strong.string, soup.strong.text) # 没用 ''

    # 4、Comment 对象
    if type(soup.strong.string) == bs4.element.Comment:
        print("这是一个注释", soup.strong.prettify(), soup.strong.string) # 这是一个注释
    else:
        print(soup.strong.string)


'''
    3、Beautiful Soup 的 find_all() 方法
        find_all() 是 Beautiful Soup 中最核心、最常用的搜索方法。
        它的作用是搜索当前标签的所有子孙节点，并返回所有符合过滤条件的结果。
        find_all(name, attrs, recursive, string, limit, **kwargs)
            name：标签名，字符串、正则表达式、列表、True
            attrs：属性，字典类型
            recursive：是否递归查找，默认 True
            string：字符串、正则表达式、列表、True
            limit：限制返回结果的数量，默认 None
            **kwargs：其他属性，键值对形式

'''
def test_bs4_find_all():
    html = '''
        <title>尚学堂</title>
        <div class='info' float='left'>Welcome to Python</div>
        <div class='info' float='right'>
            <span>Good Good Study</span>
            <a href='www.github.cn'></a>
            <strong><!--没用--></strong>
        </div>
        <h3>
            <a id=1 href='www.baidu.com'></a>
            <a id=1 href='www.github.com'></a>
            <a id=2 href='www.youtube.com'></a>
        </h3>
        '''
    soup = BeautifulSoup(html, 'lxml')

    '''
        1、查 div 标签
        得到如下：
        [<div class="info" float="left">Welcome to Python</div>,
         <div class="info" float="right">
                <span>Good Good Study</span>
                <a href="www.github.cn"></a>
                <strong><!--没用--></strong>
        </div>
        ]
    '''
    divs = soup.find_all('div')
    print(type(divs)) # <class 'bs4.element.ResultSet'>

    '''
        2、通过正则查询
    '''
    import re
    divs = soup.find_all(re.compile('div'))
    print(divs)

    '''
        3、传入列表，匹配其中的任意元素
    '''
    print(soup.find_all(['span', 'a'])) # [<span>Good Good Study</span>, <a href="www.github.cn"></a>]

    '''
        4、keyword

        传入一个 id 的参数,Beautiful Soup会搜索每个tag的”id”属性,并返回所有匹配的tag。
    '''
    print(soup.find_all(id=1)) # [<a href="www.baidu.com" id="1"></a>, <a href="www.github.com" id="1"></a>]

    '''
        5、按 class 搜索
    '''
    print(soup.find_all('div', class_='info'))

    '''
        6、按属性搜索

    '''
    print(soup.find_all('div', attrs={'float':'left'})) # [<div class="info" float="left">Welcome to Python</div>]


'''
    4、Beautiful Soup 的 select() 方法
    soup.select() 是 Beautiful Soup 提供的另一个核心搜索方法，它允许使用 CSS 选择器（CSS Selectors） 语法来定位元素。
    根据 CSS 选择器 字符串搜索当前标签下的所有子孙节点。

    | 目的           | CSS 选择器写法                    | 等效的 find_all 写法              |
    |---------------|----------------------------------|-----------------------------------|
    | 按标签名       | `soup.select('div')`              | `soup.find_all('div')`           |
    | 按 class       | `soup.select('.sister')`          | `soup.find_all(class_='sister')` |
    | 按 ID          | `soup.select('#link1')`           | `soup.find_all(id='link1')`      |
    | 按属性精确     | `soup.select('a[href="..."]')`    | `soup.find_all(href="...")`      |
    | 后代（所有）   | `soup.select('div p')`            | 需递归循环                       |
    | 子代（直接）   | `soup.select('div > p')`          | `soup.find_all('p', recursive=False)` |
    | 属性包含       | `soup.select('a[href*="x"]')`     | 需正则 `re.compile`              |
    | 属性开头       | `soup.select('a[href^="h"]')`     | 需正则                           |
    | 属性结尾       | `soup.select('a[href$=".p"]')`    | 需正则                           |
    | 组合链式       | `soup.select('div#main p.sis')`   | 多次 `find_all`                  |
'''
def test_bs4_select():
    html = """
    <html>
    <head>
        <title>示例页面</title>
    </head>
    <body>
        <div id="main">
            <h1 class="title">文章列表</h1>
            <ul class="list">
                <li><a href="/post/1" class="link" data-id="101">第一篇文章</a></li>
                <li><a href="/post/2" class="link" data-id="102">第二篇文章</a></li>
                <li><a href="/post/3" class="link special" data-id="103">第三篇（特殊）</a></li>
            </ul>
            <div class="footer">
                <p>版权所有 © 2026</p>
                <p><a href="https://example.com/about" target="_blank">关于我们</a></p>
            </div>
        </div>
    </body>
    </html>
    """
    soup = BeautifulSoup(html, 'lxml')

    print('1. 获取所有 <a> 标签 =', soup.select('a')) # 标签选择器

    print('2. 获取 class="link" 的标签 =', soup.select('.link')) # 类选择器，类为 link 的标签

    print('3. class="link special" 的标签 =', soup.select('.link.special')) # 只匹配同时拥有这两个类的标签

    print('4. id="main" 的标签 =', soup.select('#main')) # 匹配 id 选择器为 main 的标签

    print('5. href 完全等于 "/post/2" 的 a 标签 =', soup.select('a[href="/post/2"]')) # 按属性精确匹配

    print("6. div 下的所有 p 标签 =", soup.select('div p')) # 后代选择器，匹配 div 下的所有 p 标签

    print('7. body 的直接子元素 div =', soup.select('body > div')) # 子代选择器，匹配 body 的直接子元素 div

    print("8. href 包含 'post' 的 a 标签 =", soup.select('a[href*=post]')) # 属性包含(*=)

    print("9. href 以 '/post' 开头的 a 标签 =", soup.select('a[href^="/post"]')) # 属性开头(^=)

    print("10. href 以 'about' 结尾的 a 标签 =", soup.select('a[href$="about"]')) # 属性结尾($=)


    print("11. 组合链式选择器 =", soup.select('#main ul a')) # 组合链式选择器，匹配 id 为 main 的元素下的 ul 元素下的所有 a 标签

    print("12. 多条件组合，href 包含 'post' 且 class 包含 'link' 的 a 标签 =",
            soup.select('a[href*=post].link'))


def challenge():
    import requests
    from bs4 import BeautifulSoup

    url = 'http://58.87.96.193:8000/playground/1'
    resp = requests.get(url)

    soup = BeautifulSoup(resp.text)

    # 1、提取数据
    titles = soup.select('h3')
    for t in titles:
        print(t.text)

    # 2、获取子标题
    sub_titles = soup.select('h5')
    for t in sub_titles:
        print(t.text)

    # 3、获取子标题对应的内容
    contents = soup.select('div.cyber-card p') # 类属性为 cyber-card 的 div 标签下的 p 标签
    for c in contents:
        print(c.text)


if __name__ == '__main__':
    # test_bs4()

    # test_bs4_find_all()

    # test_bs4_select()

    challenge()