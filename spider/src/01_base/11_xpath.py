r"""
    数据解析 - XPath 的使用

    1、XPath 技术
        XPath 的全称是 XML Path Language（XML 路径语言）。
        简单来说，它是一种在 XML 或 HTML 文档中查找信息的“导航查询语言”。
        可以把它想象成文件系统中的路径（比如 C:\Users\Documents），
        但 XPath 更加强大——它不仅可以通过“目录结构”找东西，还可以通过“元素属性”、“文本内容”甚至“逻辑运算”来定位任何一个节点。
        官网  http://lxml.de/index.html

        核心概念：XPath 把 XML/HTML 文档看作一棵节点树（根节点、元素节点、属性节点、文本节点）。XPath 的语法就是描述从树根到某个特定树叶的“行走路线”。

    2、节点的关系
        父 Parent
        子 Children
        同胞 Sibling
        先辈 Ancestor
        后代 Descendant

    3、常用的路径表达式
        nodename -> 选取此节点的所有子节点
        /        -> 从根节点选取
        //       -> 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置
        .        -> 选取当前节点
        ..       -> 选取当前节点的父节点
        @        -> 选取属性

    4、通配符
        *        -> 匹配任何元素节点，比如 xpath('div/*') 匹配 div 元素的所有子元素
        @*       -> 匹配任何属性节点，比如 xpath('div[@*]') 匹配 div 元素的所有属性
        node()   -> 匹配任何类型的节点

    5、选取若干路径
        通过在路径表达式中使用 | 运算符，可以选取若干路径。
        xpath('//div | //span') 匹配所有的 div 元素和 span 元素。

    6、谓词
        谓词被嵌在方括号内，用来查找某个特定的节点或包含某个指定的值的节点。
        xpath('/body/div[1]')            匹配 body 元素下的第一个 div 节点。
        xpath('/body/div[last()]')       匹配 body 元素下的最后一个 div 节点。
        xpath('/body/div[last()-1]')     匹配 body 元素下的倒数第二个 div 节点。
        xpath('/body/div[@class]')       匹配 body 元素下的所有 class 属性的 div 节点。
        xpath('/body/div[@class="abc"]') 匹配 body 元素下的所有 class 属性值为 abc 的 div 节点。
        xpath('/body/div[price>35.00]')  匹配 body 元素下的所有 price 节点值大于 35.00 的 div 节点。

    7、运算符
        | 运算符 | 描述 | 示例表达式 | 返回结果 / 逻辑判断 |
        | :---: | :---: | :---: | :---: |
        | `+` | 加法 | `6 + 4` | `10` |
        | `–` | 减法 | `6 – 4` | `2` |
        | `*` | 乘法 | `6 * 4` | `24` |
        | `div` | 除法 | `8 div 4` | `2` |
        | `=` | 等于 | `price = 9.80` | `price = 9.80` 返回 `true`；`price = 9.90` 返回 `false` |
        | `!=` | 不等于 | `price != 9.80` | `price = 9.90` 返回 `true`；`price = 9.80` 返回 `false` |
        | `<` | 小于 | `price < 9.80` | `price = 9.00` 返回 `true`；`price = 9.90` 返回 `false` |
        | `<=` | 小于或等于 | `price <= 9.80` | `price = 9.00` 返回 `true`；`price = 9.90` 返回 `false` |
        | `>` | 大于 | `price > 9.80` | `price = 9.90` 返回 `true`；`price = 9.80` 返回 `false` |
        | `>=` | 大于或等于 | `price >= 9.80` | `price = 9.90` 返回 `true`；`price = 9.70` 返回 `false` |
        | `or` | 或 | `price = 9.80 or price = 9.70` | `price = 9.80` 返回 `true`；`price = 9.50` 返回 `false` |
        | `and` | 与 | `price > 9.00 and price < 9.90` | `price = 9.80` 返回 `true`；`price = 8.50` 返回 `false` |
        | `mod` | 计算除法的余数 | `5 mod 2` | `1` |

    8、选择 XML 中的节点
        element -> 元素节点
        attribute -> 属性节点
        text()  -> 文本节点
        concat(元素节点, 元素节点)
        comment -> 注释节点
        root -> 根节点

    9、XPath 工具
        XPath Parser 浏览器插件
        浏览器在元素的界面下 Ctrl + F 在搜索框可以通过 XPath 查找
        浏览器控制台 - $x(Xpath表达式) 比如：$x('//span[@class="title-content-title"]') 查找 class 属性为 title-content-title 的 span 标签
"""

import requests
from lxml import etree

def test_xpath():
    url = 'http://58.87.96.193:8000/playground/1'
    resp = requests.get(url)

    # 创建 etree 对象
    etr = etree.HTML(resp.text)

    # 提取数据
    titles = etr.xpath('//h3[@class="cyber-title"]/text()') # 获取 class 属性为 cyber-title 的 h3 标签的文本内容
    for t in titles:
        print(t)

    # 获取子标题
    sub_titles = etr.xpath('//h5/text()') # 获取所有 h5 标签的文本内容
    for t in sub_titles:
        print(t)

    # 获取子标题对应的内容
    contents = etr.xpath('//div[@class="cyber-grid"]/div[@class="cyber-card"]/p/text()') # 获取类属性为 cyber-grid 的 div 标签下的所有 p 标签的文本内容
    for c in contents:
        print(c)

    # 获取段落信息
    articles = etr.xpath('//p[@class="article-text"]/text()') # 获取类属性为 article-text 的 p 标签的文本内容
    for a in articles:
        print(a)


def practice_xpath():
    content = ""
    with open('src/spider/xpath.html', 'r', encoding='utf-8') as f:
        content = f.read()

    etr = etree.HTML(content)

    # 1、获取商品名称
    products = etr.xpath('//div[@id="product-list"]/div[@class and @data-id]/h2/a[@href]/text()')
    for p in products:
        print(p)

    # 2、获取商品链接
    links = etr.xpath('//div[@id="product-list"]/div[@class and @data-id]/h2/a[@href]') # 先获取节点元素，后面通过 get('href') 获取属性
    links = etr.xpath('//div[@id="product-list"]/div[@class and @data-id]/h2/a/@href')  # 直接获取 href 属性
    for i in links:
        # print(i.get("href"))
        print(i)

    # 3、获取商品 id
    ids = etr.xpath('//div[@id="product-list"]/div[@class and @data-id]/@data-id') # 直接获取 data-id 属性
    for i in ids:
        print(i)

    # 4、获取库存大于 0 的商品名称
    products = etr.xpath('//div[@id="product-list"]/div[@class and @data-id and @data-stock>0]/h2/a/text()')
    for p in products:
        print(p)

    # 5、获取 class 中包含 hot 的商品名称
    products = etr.xpath('//div[@id="product-list"]/div[@class and contains(@class, "hot")]/h2/a/text()')
    print(products)

    # 6、获取带有原价的商品名称
    # products = etr.xpath('//div[@id="product-list"]/div[@class and @data-id]/div[@class="price-info"]/span[@class="original-price"]/../../h2/a/text()')
    products = etr.xpath('//div[@id="product-list"]/div[div[@class="price-info"]/span[@class="original-price"]]/h2/a/text()')
    print(products)

    # 7、获取阅读量大于 2000 的文章标题
    titles = etr.xpath(
        '//div[@id="articles"]/div[@class="article" and number(substring-after(span[@class="views"]/text(), "阅读：")) > 2000]/a/text()'
    )
    print([i.strip() for i in titles])


if __name__ == '__main__':
    # test_xpath()
    practice_xpath()