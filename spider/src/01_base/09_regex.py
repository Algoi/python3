'''
    1、正则表达式
        正则表达式是一种用于匹配字符串的模式，常用于数据提取和文本处理。
        在标记语言中，正则表达式可以用于匹配特定的标签、属性或内容，从而实现对文本的筛选和提取。

    开始标记
    │
    │
    ▼
    ^[a-z0-9_-]{3,10}$
            ▲     ▲  ▲
            │     │  │
            │     │  └──────────── 结束标记
            │     │
            │     │
            └─────│─ 字母(a-z) 数字(0-9) 下划线_ 连字符-
                  │
                  │
                  │
            3~10个字符的长度
'''

'''
    2、规则
        2.1 定位符
            ^  -> 匹配输入字符串开始的位置。如果设置了 RegExp 对象的 Multiline 属性，^ 还会与 \n 或 \r 之后的位置匹配
            $  -> 匹配输入字符串结尾的位置。如果设置了 RegExp 对象的 Multiline 属性，$ 还会与 \n 或 \r 之前的位置匹配
            \b -> 匹配一个单词边界，即字与空格间的位置
            \B -> 非单词边界匹配

        2.2 普通字符
            [ABC]  -> 匹配 [...] 中的所有字符，例如 [aeiou] 匹配字符串 'google runoob taobao' 中所有的 a e i o u 字字符
            [^ABC] -> 匹配除了 [...] 中的所有字符，例如 [^aeiou] 匹配字符串 'google runoob taobao' 中所有的非 a e i o u 字符
            [A-Z]  -> 表示一个区间，匹配所有大写字母；[a-z] 匹配所有小写字母；[0-9] 匹配所有数字
            .      -> 匹配除换行符 \n \r 之外的任何单个字符，相当于 [^\n\r]
            [\s\S] -> 匹配所有。\s 是匹配所有空白符，包括换行，\S 匹配非空白符，不包括换行
            \w     -> 匹配字母、数字、下划线。等价于 [A-Za-z0-9_]

        2.3 特殊字符
            () -> 标记一个子表达式的开始和结束位置。子表达式可以获取供以后使用
            [  -> 标记一个中括号表达式的开始。要匹配 [ 本身，需要使用 \[ 转义
            ?  -> 匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。要匹配 ? 本身需要使用 \? 转义
            \  -> 将下一个字符标记为特殊字符、原意字符、向后引用、或八进制转义符。例如， \n 匹配换行符
            {  -> 标记限定符表达式的开始。要匹配 { 本身，需要使用 \{ 转义
            |  -> 指明两项之间的一个选择。要匹配 | 本身，需要使用 \| 转义

        2.4 限定符
            * -> 匹配前面的子表达式零次或者多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于 {0,}
            + -> 匹配前面子表达式一次或多次。例如，zo+ 能匹配 "zo" 以及 "zoo" 等。但不能匹配 'z'
            ? -> 匹配前面的子表达式零次或一次。例如，do(es)? 能匹配 "do" 以及 "does"。? 等价于 {0,1}
            {n} -> n 是一个非负整数。匹配确定的 n 次。例如，o{2} 能匹配 "Bob" 中的两个 o，但不能匹配 "Bob" 中的一个 o
            {n, } -> n 是一个非负整数。至少匹配 n 次。例如，o{2,} 能匹配 "Boo" 中的两个 o，也能匹配 "Booo" 中的三个 o
            {n, m} -> m 和 n 均为非负整数，其中 n <= m。最少匹配 n 次且最多匹配 m 次。例如，o{1, 3} 能匹配 "o"、"oo" 或 "ooo"
            注意：限定符和定位符不能一起使用。

        2.5 非打印字符
            \cx -> 匹配由 x 指明的控制字符。例如，\cM 匹配一个 Control-M 或回车符。x 的值必须为 A-Z 或 a-z 之一。
            \f  -> 匹配一个换页符。等价于 \x0c 和 \cL
            \n  -> 匹配一个换行符。等价于 \x0a 和 \cJ
            \r  -> 匹配一个回车符。等价于 \x0d 和 \cM
            \s  -> 匹配任何空白字符，包括空格、制表符、换页符等。等价于 [\f\n\r\t\v]
            \S  -> 匹配任何非空白字符。等价于 [^\f\n\r\t\v]
            \t  -> 匹配一个制表符。等价于 \x09 和 \cI
            \v  -> 匹配一个垂直制表符。等价于 \x0b 和 \cK
'''

'''
    3、数量词的贪婪模式和非贪婪模式
        当同一个位置可以有多种匹配长度时，到底是尽量匹配更多，还是尽量匹配更少。
        在 python 的正则里，数量词默认都是贪婪的。

        在下面 regex_greedy() 函数中测试
'''

# 引入正则模块，在标准库中
import re

def regex_match():
    '''
        从头开始匹配，如果匹配上了返回值，如果匹配不上，返回none
        re.match 匹配一个与表达式相符数据
        re.match(pattern, string, flags=0)
    '''

    info = 'I study python3.14 every_day'

    m1 = re.match(r'python', info) # 匹配字符串开头
    print(m1) # None

    m2 = re.match(r'\w+', info) # 匹配字符串开头的一个或多个字母、数字、下划线。等价于 [A-Za-z0-9_]+
    print(m2) # <re.Match object; span=(0, 1), match='I'>

    m3 = re.match(r'\S+', info) # 匹配字符串开头的一个或多个非空白字符。等价于 [^\f\n\r\t\v]+
    print(m3) # <re.Match object; span=(0, 1), match='I'>

    m4 = re.match(r'\D', info) # 匹配字符串开头的一个非数字字符。等价于 [^0-9]。\d 表示匹配一个数字字符。等价于 [0-9]
    print(m4) # <re.Match object; span=(0, 1), match='I'>

    m5 = re.match(r'I (study)', info) # 匹配字符串开头的 'I study'，并捕获 'study' 作为一个子表达式
    print(m5, m5.group(1)) # <re.Match object; span=(0, 9), match='I study'> study

    m6 = re.match(r'\w\s(\w+)', info)
    print(m6, m6.group(1)) # <re.Match object; span=(0, 9), match='I study'> study

    m7 = re.match(r'(\w+\s){2}(.+)\s', info)
    print(m7, m7.group(2)) # <re.Match object; span=(0, 17), match='I study python3.14 '> python3.14


def regex_search():
    '''
        在整个字符串中搜索匹配，如果匹配上了返回值，如果匹配不上，返回none
        re.search 匹配一个与表达式相符数据
        re.search(pattern, string, flags=0)
    '''

    info = 'I study python3.14 every_day'

    s1 = re.search(r'I', info)
    print(s1) # <re.Match object; span=(0, 1), match='I'>

    s2 = re.search(r'python', info)
    print(s2) # <re.Match object; span=(8, 14), match='python'>

    s3 = re.search(r'\w+(\d\.\d+)', info) # 提取版本号 3.14
    print(s3, s3.group(1)) # <re.Match object; span=(14, 20), match='3.14'> 3.14

    s4 = re.search(r'p\D+', info) # 匹配以 p 开头的一个或多个非数字字符。等价于 [^0-9]+ 这里会提取 python
    print(s4, s4.group()) # <re.Match object; span=(8, 14), match='python'> python


def regex_findall():
    '''
        在整个字符串中搜索匹配，返回所有匹配的结果，返回一个列表
        re.findall 匹配所有与表达式相符数据
        re.findall(pattern, string, flags=0)
    '''

    info = 'I study python3.14 every_day'

    f1 = re.findall(r'\w+', info) # 匹配一个或多个字母、数字、下划线。等价于 [A-Za-z0-9_]+
    print(f1) # ['I', 'study', 'python3', '14', 'every_day']

    f2 = re.findall(r'\d+', info) # 匹配一个或多个数字字符。等价于 [0-9]+
    print(f2) # ['3', '14']


def regex_sub():
    '''
        替换原来的数据，并返回一个新的字符串，不会修改原来的字符串。
        re.sub(pattern, replace, string)
    '''
    info = 'I study python3.14 every_day'

    s1 = re.sub(r'\d\.\d+', '3.12', info)
    print(s1) # I study python3.12 every_day

    s2 = re.sub(r'\w+\.\d+', 'java8', info)
    print(s2) # I study java8 every_day


def regex_greedy():
    '''
        测试贪婪和非贪婪

        贪婪模式：尽可能多的匹配字符
        非贪婪模式：尽可能少的匹配字符

        Python 正则默认贪婪；在数量限定符后面加 ?，就变成非贪婪。
        限定符        贪婪        非贪婪
        --------------------------------
        *             *           *?
        +             +           +?
        ?             ?           ??
        {n,m}         {n,m}       {n,m}?
    '''
    text = '<a>百度</a><a>Github</a>'
    print(re.findall(r'<a>.*?</a>', text))

def test_html():
    '''
        正则表达式在标记语言中，常用于匹配特定的标签、属性或内容，从而实现对文本的筛选和提取。
    '''
    html = '''
        <html>
            <head>
                <title>My First HTML</title>
            </head>
            <body>
                <h1>My First Heading</h1>
                <p>My first paragraph.</p>
                <a href="https://www.github.com">Example github Link</a>
                <a href="https://www.baidu.com">Example baidu Link</a>
            </body>
        </html>
    '''

    # 贪婪 .* vs 非贪婪 .*?
    hrefs = re.findall(r'<a href="(.*?)">', html)
    print(hrefs) # ['https://www.github.com', 'https://www.baidu.com']


'''
    实战
'''
import re # python内置

import requests # 第三方模块 在后面

'''
    4、知识点补充 - 可选标志
    正则表达式可以包含一些可选标志来控制匹配的模式。
    修改符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 来指定。

    re.l  -> 匹配对大小写不敏感
    re.L  -> 做本地化识别匹配
    re.M  -> 使边界字符 ^ 和 $ 匹配每一行的开头和结尾，记住是多行，而不是整个字符串的开头和结尾
    re.S  -> 使 . 匹配包括换行在内的所有字符
    re.U  -> 根据 Unicode 字符集解析字符，这个标志影响 \w \W \b \B
    re.X  -> 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解
'''

def challenge():
    resp = requests.get('http://58.87.96.193:8000/playground/1')

    content = resp.text

    print(re.search('<h3 class="cyber-title">(.+?)</h3>', content).group(1)) # 标签中的内容就是标题，使用非贪婪模式

    '''
    <div class="cyber-card">
        <i class="fas fa-heartbeat cyber-icon"></i>
        <h5>医疗保健</h5>
        <p>AI 辅助诊断和药物研发</p>
    </div>
    '''
    print(re.findall(r'<div class="cyber-card">.*?<h5>(.+?)</h5>.*?<p>(.+?)</p>.*?</div>', content, re.S)) # re.S 让 . 匹配换行符


'''
    练习
'''
def practice():
    text = '商品编号: 1024，价格: 299 元，库存: 35 件'
    print(re.findall(r'\d+', text)) # ['1024', '299', '35']


    text = '''
    Python2.7 已停止维护
    Python3.10 很稳定
    Python3.12 性能更好
    Python3.14 即将发布
    '''
    print(re.findall(r'(\d\.\d+)', text)) # ['2.7', '3.10', '3.12', '3.14']


    html = '''
    <html>
    <head>
        <title>Python 爬虫教程</title>
    </head>
    <body>
    </body>
    </html>
    '''
    print(re.search(r'<title>(.+?)</title>', html).group(1)) # Python 爬虫教程

    html = '''
    <a href="https://www.baidu.com">百度</a>
    <a href="https://www.github.com">Github</a>
    <a href="https://www.python.org">Python</a>
    '''
    print(re.findall(r'a href="(.+?)">(.+?)</a>', html))
    # [('https://www.baidu.com', '百度'),
    #  ('https://www.github.com', 'Github'),
    #  ('https://www.python.org', 'Python')]


    html = '''
    <div class="news">
        <a href="/news/1001">
            <h3>Python 3.14 发布新版本</h3>
            <span class="time">2026-09-01</span>
        </a>
    </div>

    <div class="news">
        <a href="/news/1002">
            <h3>人工智能行业持续发展</h3>
            <span class="time">2026-09-02</span>
        </a>
    </div>

    <div class="news">
        <a href="/news/1003">
            <h3>Linux 内核发布更新</h3>
            <span class="time">2026-09-03</span>
        </a>
    </div>
    '''
    pattern = r'<div class="news">.*?<a href="(.+?)">.*?<h3>(.+?)</h3>.*?<span class="time">(.+?)</span>.*?</a>'
    print(re.findall(pattern, html, re.S))
    # [('/news/1001', 'Python 3.14 发布新版本', '2026-09-01'),
    #  ('/news/1002', '人工智能行业持续发展', '2026-09-02'),
    #  ('/news/1003', 'Linux 内核发布更新', '2026-09-03')]


if __name__ == '__main__':
    # regex_match()
    # regex_search()
    # regex_findall()
    # regex_sub()
    regex_greedy()
    # test_html()

    # challenge()

    # practice()


