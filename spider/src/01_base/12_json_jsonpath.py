'''
    1、JSON 数据使用
        JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，更容易理解和阅读。
        适用于前后端的数据交互。

        Python 自带 json 模块，直接 import json 即可使用。
        官方文档 http://docs.python.org/library/json.html

        json简单说就是javascript中的对象和数组，
        所以这两种结构就是对象和数组两种结构，通过这两种结构可以表示各种复杂的结构。

        1.1 JSON 对象
            对象在js中表示为{ }括起来的内容，数据结构为 { key: value, key: value, ... }的键值对的结构。
            在面向对象的语言中，key为对象的属性，value为对应的属性值。
            取值方法为 对象.key 获取属性值，这个属性值的类型可以是数字、字符串、数组、对象这几种

        1.2 JSON 数组
            数组在js中是中括号[ ]括起来的内容，数据结构为 ["Python", "javascript", "C++", ...]，
            取值方式和所有语言中一样，使用索引获取，字段值的类型可以是 数字、字符串、数组、对象几种

    2、Python 中的 json 模块
        json 模块提供了四个函数：
            json.dump()：将 Python 对象编码转换为 JSON 对象，并写入文件。
            json.dumps()：将 Python 对象编码转换为 JSON 对象，并返回字符串。
            json.load()：从文件中读取 JSON 对象，并解码为 Python 对象。
            json.loads()：从字符串中读取 JSON 对象，并解码为 Python 对象。
'''


import json

def test_json_loads():
    str_list = '[1, 2, 3, 4, 5]'
    res = json.loads(str_list)
    print(res, type(res)) # [1, 2, 3, 4, 5] <class 'list'>

    str_dict = '{"姓名": "Python", "年龄": 30, "language": ["Python", "JavaScript", "C++"]}'
    res = json.loads(str_dict)
    print(res, type(res)) # {'姓名': 'Python', '年龄': 30, 'language': ['Python', 'JavaScript', 'C++']} <class 'dict'>

def test_json_dumps():
    dict_data = {"姓名": "Python", "年龄": 30, "language": ["Python", "JavaScript", "C++"]}
    res = json.dumps(dict_data, ensure_ascii=False) # ensure_ascii=False 可以保证中文不被转义
    print(res, type(res)) # {"姓名": "Python", "年龄": 30, "language": ["Python", "JavaScript", "C++"]} <class 'str'>

    tup_data = ("Python", "JavaScript", "C++")
    res = json.dumps(tup_data)
    print(res, type(res)) # ["Python", "JavaScript", "C++"] <class 'str'>

    list_data = ["Python", "JavaScript", "C++"]
    res = json.dumps(list_data)
    print(res, type(res)) # ["Python", "JavaScript", "C++"] <class 'str'>


def test_json_dump():
    list_str = [{"city": "北京"}, {"name": "范爷"}]
    json.dump(list_str, open("src\\spider\\json_dump_list_str.json", "w"), ensure_ascii=False)

    dict_str = {"city": "北京", "name": "范爷"}
    json.dump(dict_str, open("src\\spider\\json_dump_dict_str.json", "w"), ensure_ascii=False)


def test_json_load():
    str_list = json.load(open("src\\spider\\json_dump_list_str.json","r"))
    print(str_list, type(str_list)) # [{'city': '北京'}, {'name': '范爷'}] <class 'list'>

    dict_str = json.load(open("src\\spider\\json_dump_dict_str.json","r"))
    print(dict_str, type(dict_str)) # {'city': '北京', 'name': '范爷'} <class 'dict'>


'''
    3、注意事项
        json.loads() 是把 json 格式字符串解码转换成 python 对象，如果 json.loads() 的时候出错，要注意被解码的 json 字符的编码。
        如果传入的字符串编码不是 utf-8，在进行 loads 之前需要使用相同的字符集解码，再进行 loads
'''
def test_json_loads_encoding():
    str_dict = '{"姓名": "Python", "年龄": 30, "language": ["Python", "JavaScript", "C++"]}'
    str_gbk = str_dict.encode("gbk") # 将字符串编码为 gbk
    res = json.loads(str_gbk.decode('gbk')) # 先把字符串解码，按照指定的编码格式
    print(res, type(res)) # {'姓名': 'Python', '年龄': 30, 'language': ['Python', 'JavaScript', 'C++']} <class 'dict'>


r'''
    4、JSONPath 模块
        JsonPath 是一种信息抽取类库，是从JSON文档中抽取指定信息的工具，提供多种语言实现版本，
        包括：Python，Javascript， PHP和 Java。
        JsonPath 对于 JSON 来说，相当于 XPATH 对于 HTML
        官网 http://goessner.net/articles/JsonPath

        | XPath       | JSONPath       | 描述
        | :---------: | :------------: | :-----------------------------------------------------------------
        | `/`         | `$`            | 根节点
        | `.`         | `@`            | 当前节点
        | `/`         | `.` 或 `[]`    | 取子节点
        | `..`        | `n/a`          | 取父节点，JSONPath 未支持
        | `//`        | `..`           | 不管位置，选择所有符合条件的条件
        | `*`         | `*`            | 匹配所有元素节点
        | `@`         | `n/a`          | 根据属性访问，JSON 不支持（因为 JSON 是 Key-Value 递归结构，不需要）
        | `[]`        | `[]`           | 迭代器标示（可在其中做简单的迭代操作，如数组下标、根据内容选值等）
        | `\|`        | `[,]`          | 支持迭代器中做多选
        | `[]`        | `?()`          | 支持过滤操作
        | `n/a`       | `()`           | 支持表达式计算
        | `()`        | `n/a`          | 分组，JSONPath 不支持

        注意：jsonpath 表达式要从 $ 开头
'''

from jsonpath import jsonpath
import requests

def test_jsonpath():
    url = 'http://58.87.96.193:8000/api/movies?page=1&movie_type=&movie_time='
    resp = requests.get(url)

    data = resp.json() # 这个响应是 json 数据，直接使用 json() 转换过来

    movie_name = jsonpath(data, '$..movie_name')
    movie_type = jsonpath(data,'$..movie_type')
    for title,type in zip(movie_name, movie_type):
        print(title,'=====',type)


if __name__ == '__main__':
    # test_json_loads()
    # test_json_dumps()
    # test_json_dump()
    # test_json_load()

    # test_json_loads_encoding()

    test_jsonpath()