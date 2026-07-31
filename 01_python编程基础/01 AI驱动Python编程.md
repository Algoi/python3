# 01 AI驱动Python编程

# Python 入门

## Python 是什么\-\-\-应用范围

### Python 特点

Python 是最流行的程序设计语言，由荷兰人，吉多·范罗苏姆 1989 年发明，1991年公布。

- 可读性强

- 简洁

- 开源：纯粹的开源语言，软件移植性强

- 标准的脚本语言

### Python 应用场景

- 人工智能领域的王者

- web应用开发（web框架，如 Django，TurboGears等）

- 操作系统管理、服务器运维的自动化脚本

- 科学计算和数据分析（Numpy、Matplotlib 等库可以编写科学计算程序）

- 桌面软件（PyQt 可以快速开发桌面程序）

- 服务器软件、网络爬虫

- 游戏开发

### Python 版本和兼容问题

- Python 有两大版本，分别是 python 2\.x 和 python 3\.x

- Python 2\.x 在 2020 年已经停止支持，3\.x 是主流

- Python 3\.x 2008 年发布，完全不兼容 2\.x

- Python3 的很多新特性也被移植到了 Python2\.7，作为过渡。如果程序可以在 2\.7 运行，可以通过一个名为 2to3（Python自带的一个脚本）的转换工具无缝迁移到Python3

## 正确的学习方法

- 关键在坚持

- 守破离的学习战略

> 守：学习期间，照着老师的做，不急功近利，不怀疑老师
> 
> 破：工作后，开始突破，怀疑老师，自己构建知识体系
> 
> 离：彻底脱离老师，自成体系
> 
> 

- 建立知识体系为第一要务

> 按照学习计划尽快搭建知识体系
> 
> 如果有知识点不懂，记住结论，先往后学
> 
> 

- 不追求完美主义

> 不追求每个知识点都 100% 掌握，70% 左右就不错了
> 
> 掌握每个知识点最常见的用法，不要死磕不常见的用法
> 
> 

## Python 程序基本格式

- 恰当的空格，缩进问题

    1. 通过行首缩进决定代码行的分组

    2. 语句从新行的第一列开始

- 缩进风格统一

    1. 每个缩进层次使用 **单个制表符 或 四个空格**

    2. Python 使用 1 个或多个缩进层次来表达程序块的层次

- Python 区分大小写

- 注释 （是程序中会被 python 解释器忽略的一段文本，用于说明代码的作用等信息）

    - 单行注释（使用 \# ）

    - 段注释/多行注释（三个连续单引号 或 三个双引号）

        连续三个引号，其实就是定义了一个字符串，只不过没有变量指向它，从而被当作垃圾忽略了。

    ```Python
    # 单行注释
    print("单行注释")
    
    '''
    三个连续单引号
    可以用于实现多行注释
    作者：
    时间：
    '''
    print('三个连续单引号可以用于实现多行注释')
    
    """
    三个双引号实现多行注释
    作者:
    时间:
    """
    print('双引号实现多行注释')
    ```

## Turtle 库绘图

```Python
import turtle # 导入 turtle 模块

turtle.showturtle() # 显示箭头

turtle.write('起点') # 写字符串

turtle.forward(300) # 向前 300 像素，x 轴方向

turtle.color('red') # 画笔颜色改为 red

turtle.left(90) # 箭头向左转 90 度

turtle.forward(300) # 朝着箭头方向前进 300 像素

turtle.goto(0, 50) # 去坐标 (0, 50)
turtle.goto(0, 0)

turtle.penup() # 抬笔，就不会画线了
turtle.goto(0, 300) # 去到 (0, 300) 位置，中途不会再画线了
turtle.pendown() # 下笔，之后再移动画笔就会继续绘画

turtle.circle(100) # 画一个半径为 100 的圆

turtle.done() # 程序结束，窗口保持存在
```

![PixPin\_2026\-07\-20\_23\-20\-02\.png](图片和附件/PixPin_2026-07-20_23-20-02.png)

```Go
import turtle

turtle.width(6)
turtle.hideturtle() # 隐藏箭头

# 第一个圆形
turtle.color('blue')
turtle.circle(100)


# 第二个圆形
turtle.penup()
turtle.goto(160, 0)
turtle.pendown()
turtle.color('green')
turtle.circle(100)

# 第三个圆形
turtle.penup()
turtle.goto(320, 0)
turtle.pendown()
turtle.color('red')
turtle.circle(100)

# 第四个圆形
turtle.penup()
turtle.goto(80, -100)
turtle.pendown()
turtle.color('yellow')
turtle.circle(100)

# 第五个圆形
turtle.penup()
turtle.goto(240, -100)
turtle.pendown()
turtle.color('black')
turtle.circle(100)

turtle.done()
```

![PixPin\_2026\-07\-20\_23\-42\-59\.png](图片和附件/PixPin_2026-07-20_23-42-59.png)

# AI 助力 python 开发

# 编程基本概念

## Python 程序的构成和代码块组织

> 1. Python 程序由模块构成，一个模块就是一个 py 源文件，文件后缀是 \.py
> 
> 2. 模块由语句组成，运行时逐行运行这些 py 语句
> 
> 3. 语句是基本单元，用于创建对象、变量赋值、流程控制、调用函数等等
> 
> 程序员第一习惯：保存代码 ctrl \+ s
> 
> 

![PixPin\_2026\-07\-21\_07\-57\-35\.png](图片和附件/PixPin_2026-07-21_07-57-35.png)

> Python官方推荐的PEP\-8代码风格详细说明，可参考： https://www\.python\.org/dev/peps/pep\-0008/
> 
> 

![PixPin\_2026\-07\-21\_08\-13\-51\.png](图片和附件/PixPin_2026-07-21_08-13-51.png)

![PixPin\_2026\-07\-21\_08\-12\-21\.png](图片和附件/PixPin_2026-07-21_08-12-21.png)

```Python
str1 = 'hello \
world'

nums = [10, 20, 30, \
    40, 50, 60]

print(str1)
```

## 对象和内存

> Python 中一切皆对象
> 
> 对象由：标识、类型和值组成
> 
> 1. 标识 identity：唯一表示对象，通常是内存地址。使用内置函数 id\(obj\) 可获取标识
> 
> 2. 类型 type：标识对象存储的 '数据' 的类型。类型决定了对象的取值范围和可执行的操作。使用内置函数 type\(obj\) 可获取对象所属类型
> 
> 3. 值 value：表示对象所存储的信息。直接 print\(obj\) 可输出
> 
> 对象本质：一个内存块，拥有特定的值以及支持特定类型的相关操作
> 
> 

![PixPin\_2026\-07\-21\_08\-24\-16\.png](图片和附件/PixPin_2026-07-21_08-24-16.png)

```Python
var1 = 10
print(id(var1))   # 140703143667096
print(type(var1)) # <class 'int'>
print(var1)       # 10
```

![PixPin\_2026\-07\-21\_08\-35\-14\.png](图片和附件/PixPin_2026-07-21_08-35-14.png)

> 从内存图中可以看出，python 所有的对象（包括整数、字符串、列表、函数等）都存储在 堆内存（Heap） 中
> 
> 

## 引用

Python 中，变量也称为 “对象的引用”，变量存储的是对象的地址。变量则通过地址id引用对象。如上图所示。

- 变量位于栈内存（栈内存有压栈出栈操作，内存连续，速度快）

- 对象位于堆内存（内存不连续，离散，速度慢，但是空间非常大）

> 变量不需要显式声明类型（变量没有类型、对象有类型）。根据变量引用的对象，Python解释器自动确定数据类型。
> 
> 

## 标识符\_命名规则

1. 标识符规则和用法

![PixPin\_2026\-07\-21\_08\-57\-16\.png](图片和附件/PixPin_2026-07-21_08-57-16.png)

![PixPin\_2026\-07\-21\_08\-56\-12\.png](图片和附件/PixPin_2026-07-21_08-56-12.png)

2. 关键字查看

> 可以使用 help\(\) 帮助系统查看关键字，执行 help\(\) 可以进入交互窗口，然后输入 keywords 就可以查看关键字。
> 
> 

![PixPin\_2026\-07\-21\_08\-59\-37\.png](图片和附件/PixPin_2026-07-21_08-59-37.png)

3. 标识符命名规则

![PixPin\_2026\-07\-21\_09\-00\-03\.png](图片和附件/PixPin_2026-07-21_09-00-03.png)

## 变量声明\_初始化\_垃圾回收

1. 变量的声明和赋值：用于将一个变量绑定到一个对象上，格式 `变量名 = `表达式`。最简单的表达式是字面量，比如`: a = 123。在运行过程中，解释器先运行右边的表达式，生成一个代表表达式运算结果的对象，然后将对象地址赋值到左边变量。

2. 变量使用前需要被初始化，如果未被赋值，报错未定义。

![PixPin\_2026\-07\-21\_21\-03\-22\.png](图片和附件/PixPin_2026-07-21_21-03-22.png)

3. 删除变量和垃圾回收

- 可以通过 del 语句删除不再使用的变量

- 如果对象没有变量引用，就会被垃圾回收器回收，清空内存

> 删除后的变量不可继续使用，否则还会报 not defined 错误
> 
> 

![PixPin\_2026\-07\-21\_21\-07\-27\.png](图片和附件/PixPin_2026-07-21_21-07-27.png)

## 常量\_链式赋值\_系列解包赋值

1. 常量

Python 没有常量，只是逻辑上的常量。我们只能约定常量的命名规则，不对其进行修改。

```Python
MAX_SPEED = 120
print(MAX_SPEED)  # 输出 120

MAX_SPEED = 140   # 实际是可以改的。只能逻辑上不做修改。
print(MAX_SPEED)  # 输出140
```

2. 链式赋值

用于同一个对象赋值多个变量

![PixPin\_2026\-07\-21\_21\-19\-21\.png](图片和附件/PixPin_2026-07-21_21-19-21.png)

```Python
num1 = num2 = 100
print(num1, num2) # 100 100
print(id(num1), id(num2)) # 140703355875544 140703355875544
```

3. 系列解包赋值

![PixPin\_2026\-07\-21\_21\-21\-50\.png](图片和附件/PixPin_2026-07-21_21-21-50.png)

使用系列解包赋值实现变量值交换，不需要借助中间变量

```Python
n1, n2 = 10, 20
n1, n2 = n2, n1
print(n1, n2) # 20 10
```

## 内置数据类型\_基本算术运算符

![PixPin\_2026\-07\-21\_21\-35\-38\.png](图片和附件/PixPin_2026-07-21_21-35-38.png)

![PixPin\_2026\-07\-21\_21\-37\-08\.png](图片和附件/PixPin_2026-07-21_21-37-08.png)

![PixPin\_2026\-07\-21\_21\-37\-41\.png](图片和附件/PixPin_2026-07-21_21-37-41.png)

```Python
result = 7 / 2
print(result) # 3.5
result = 7 // 2 
print(result) # 3
result = 7 % 2
print(result) # 1
result = 7 ** 2
print(result) # 49

# 0 做除数会产生异常
# 7 / 0  # ZeroDivisionError: division by zero
```

```Python
# divmod() 函数可以同时得到商和余数
result = divmod(10, 3)
print(result) # (3, 1) 结果是一个元组
```

## 整数\_进制\_其他类型转整数

- Python3 中的整数任意大

Python2中， int 是32位，可以存储从 \-2147483648 到 2147483647 的整数 （约±21亿）。Long类型是64位，可以存储：\-2^63\-\-2^63\-1之间的 数值。 

Python3中， int 可以存储任意大小的整数， long 被取消。我们甚至 可以存储下面的值：

```Python
# Python3中可以做超大数的计算，而不会造成“整数溢出”，这也 是Python特别适合科学运算的特点
result = 9 ** 100
print(result) # 265613988875874769338781322035779626829233452653394495974574961739092490901302182994384699044001
```

- 三种进制数

![PixPin\_2026\-07\-21\_21\-54\-46\.png](图片和附件/PixPin_2026-07-21_21-54-46.png)

![PixPin\_2026\-07\-21\_21\-57\-17\.png](图片和附件/PixPin_2026-07-21_21-57-17.png)

- 使用 int\(\) 实现类型转换

![PixPin\_2026\-07\-21\_21\-59\-28\.png](图片和附件/PixPin_2026-07-21_21-59-28.png)

![PixPin\_2026\-07\-21\_22\-03\-19\.png](图片和附件/PixPin_2026-07-21_22-03-19.png)

![PixPin\_2026\-07\-21\_22\-03\-47\.png](图片和附件/PixPin_2026-07-21_22-03-47.png)

## 浮点数\_自动转换\_强制转换\_增强赋值运算符

![PixPin\_2026\-07\-21\_22\-48\-33\.png](图片和附件/PixPin_2026-07-21_22-48-33.png)

![PixPin\_2026\-07\-21\_22\-49\-13\.png](图片和附件/PixPin_2026-07-21_22-49-13.png)

![PixPin\_2026\-07\-21\_22\-53\-51\.png](图片和附件/PixPin_2026-07-21_22-53-51.png)

```Python
f1 = 100.999
print(f1)

f2 = float('123.123')
print(f2)

x1 = 10.234
print(round(x1)) # 10 该函数会四舍五入小数部分，不会改原来的值

x2 = 10.543
print(round(x2)) # 11

t1 = float(True)
print(t1) # 1.0
```

## 时间的表示\_unix 时间点\_毫秒微秒\_time模块

![PixPin\_2026\-07\-21\_23\-15\-06\.png](图片和附件/PixPin_2026-07-21_23-15-06.png)

![PixPin\_2026\-07\-21\_23\-17\-20\.png](图片和附件/PixPin_2026-07-21_23-17-20.png)

```Python
import time

cur = time.time()
print(cur) # 1784647221.0126579

cur = int(cur)
print(cur) # 1784647221

totalMinutes = cur // 60
print(totalMinutes) # 29744120

totalHours = totalMinutes // 60
print(totalHours) # 495735

totalDays = totalHours // 24
print(totalDays) # 20655

totalYears = totalDays // 365 # 忽略闰年
print(totalYears) # 56
```

## 多点坐标\_计算距离

```Python
import turtle
import math

# 使用系列解包赋值初始化坐标变量
x1, y1 = 100, 100
x2, y2 = 100, -100
x3, y3 = -100, -100
x4, y4 = -100, 100

# 将坐标连线
turtle.hideturtle()
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)
turtle.goto(x3, y3)
turtle.goto(x4, y4)

# 计算起点和终点的距离
# math.sqrt 函数返回值是平方根，float 类型
distance = math.sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
print("distance =", distance)

turtle.done()
```

## 布尔值本质\_逻辑运算符\_位运算符\_比较运算符\_短路问题

1. 布尔值的本质

![PixPin\_2026\-07\-22\_07\-54\-19\.png](图片和附件/PixPin_2026-07-22_07-54-19.png)

![PixPin\_2026\-07\-22\_07\-39\-44\.png](图片和附件/PixPin_2026-07-22_07-39-44.png)

```Python
a = True
b = 3
c = a + b

print(a) # True
print(c) # 4

# bool() 函数可以把值转为对应的布尔类型的值
print('空字符串的布尔类型的值 =', bool('')) # False
print('空列表布尔类型的值 =', bool([])) # False
print('None布尔类型的值 =', bool(None)) # False
print('0布尔类型的值 =', bool(0)) # False
print('字符串True和False转成布尔类型的值都是 True =', bool('False')) # True
```

2. 逻辑运算符

![PixPin\_2026\-07\-22\_07\-48\-29\.png](图片和附件/PixPin_2026-07-22_07-48-29.png)

```Python
a, b, c = 1, 2, 3
print((a < b) and (b < c)) # True
print((a > b) or (c > b)) # True
print(not(a > b)) # True
```

3. 比较运算符

![PixPin\_2026\-07\-22\_07\-53\-15\.png](图片和附件/PixPin_2026-07-22_07-53-15.png)

```Python
a = 5

print( 0 < a < 10) # python 允许连用关系运算符，相当于 a > 0 and a < 10
```

4. 位运算符

![PixPin\_2026\-07\-22\_07\-59\-48\.png](图片和附件/PixPin_2026-07-22_07-59-48.png)

5. \+ 和 \* 运算符的补充

> 与 C 和 JAVA 不一样， Python 不支持自增\(\+\+\)和自减\(\-\-\)
> 
> 

![PixPin\_2026\-07\-22\_08\-03\-40\.png](图片和附件/PixPin_2026-07-22_08-03-40.png)

6. 增强赋值运算符（补充）

![PixPin\_2026\-07\-22\_08\-05\-38\.png](图片和附件/PixPin_2026-07-22_08-05-38.png)

## 同一运算符\_成员运算符\_优先级

1. 同一运算符

![PixPin\_2026\-07\-22\_08\-12\-32\.png](图片和附件/PixPin_2026-07-22_08-12-32.png)

2. 数据缓存问题

![PixPin\_2026\-07\-22\_08\-14\-31\.png](图片和附件/PixPin_2026-07-22_08-14-31.png)

![PixPin\_2026\-07\-22\_08\-24\-31\.png](图片和附件/PixPin_2026-07-22_08-24-31.png)

> 1. is 比较两个对象的 id 值是否相等，是否指向同一个内存地址
> 
> 2. == 比较的是两个对象的内容是否相等，值是否相等 
> 
> 3. is 运算符比 == 效率高，在变量和 None 进行比较时，应该使用 is
> 
> 

3. 成员运算符

![PixPin\_2026\-07\-22\_08\-29\-24\.png](图片和附件/PixPin_2026-07-22_08-29-24.png)

4. 运算符优先级

![PixPin\_2026\-07\-22\_08\-30\-36\.png](图片和附件/PixPin_2026-07-22_08-30-36.png)

![PixPin\_2026\-07\-22\_08\-32\-03\.png](图片和附件/PixPin_2026-07-22_08-32-03.png)

## 字符串

### 字符串\_unicode字符集\_三种创建字符串的方式\_len\(\)函数

1. 字符串基本特点

> - 字符串的本质是**字符序列**
> 
> - Python 不支持单字符类型，单字符也被作为字符串使用
> 
> - Python 中的字符串是不可变的，无法对原字符串做任何修改。对字符串操作使其变化其实是新的字符串，不是原来的。
> 
> 

2. 字符串编码

![PixPin\_2026\-07\-22\_21\-29\-26\.png](图片和附件/PixPin_2026-07-22_21-29-26.png)

![PixPin\_2026\-07\-22\_21\-32\-52\.png](图片和附件/PixPin_2026-07-22_21-32-52.png)

3. 字符串的创建方式

```Python
# 1、单引号创建字符串
str1 = 'hello'
print(str1)

# 2、双引号创建字符串
str2 = "world"
print(str2)

# 3、三引号创建字符串
str3 = '''python'''
str4 = """java"""
print(str3)
print(str4)
```

![PixPin\_2026\-07\-22\_21\-52\-16\.png](图片和附件/PixPin_2026-07-22_21-52-16.png)

4. 空字符串和 len\(\) 函数

![PixPin\_2026\-07\-22\_23\-16\-53\.png](图片和附件/PixPin_2026-07-22_23-16-53.png)

### 转义字符\_字符串拼接\_字符串复制\_input\(\)获取键盘输入

![PixPin\_2026\-07\-22\_23\-00\-20\.png](图片和附件/PixPin_2026-07-22_23-00-20.png)

![PixPin\_2026\-07\-22\_23\-04\-59\.png](图片和附件/PixPin_2026-07-22_23-04-59.png)

```Python
a = 'ab''cd'
print(a) # abcd
```

![PixPin\_2026\-07\-22\_23\-06\-39\.png](图片和附件/PixPin_2026-07-22_23-06-39.png)

![PixPin\_2026\-07\-22\_23\-08\-37\.png](图片和附件/PixPin_2026-07-22_23-08-37.png)

![PixPin\_2026\-07\-22\_23\-12\-44\.png](图片和附件/PixPin_2026-07-22_23-12-44.png)

![PixPin\_2026\-07\-22\_23\-14\-46\.png](图片和附件/PixPin_2026-07-22_23-14-46.png)

### **str\(\)\_字符提取\_replace\(\)替换\_内存分析**

1. str\(\) 转字符串

![PixPin\_2026\-07\-23\_08\-56\-50\.png](图片和附件/PixPin_2026-07-23_08-56-50.png)

2. replace\(\) 函数实现字符串替换

> 字符串是“不可改变”的，我们通过\[\]可以获取字符串指定位置的字 符，但是我们不能改变字符串。
> 
> 

![PixPin\_2026\-07\-23\_09\-01\-45\.png](图片和附件/PixPin_2026-07-23_09-01-45.png)

> 字符串不可改变。但是，我们确实有时候需要替换某些字符。这 时，只能通过创建新的字符串来实现。replace 函数可以实现这个功能，这个 replace 的过程其实是创建了新的字符串，str1 指向了新的字符串对象。
> 
> 

```Python
str1 = "abcd"
str1 = str1.replace("a", "x") # 替换
print(str1) # xbcd
```

3. 使用 \[\] 提取字符

![PixPin\_2026\-07\-23\_09\-06\-44\.png](图片和附件/PixPin_2026-07-23_09-06-44.png)

```Python
str1 = "abcd"

print(str1[0], str1[1], str1[2], str1[len(str1) - 1]) # a b c d
# print(str1[len(str1)]) # IndexError: string index out of range

print(str1[-1], str1[-2], str1[-3], str1[-len(str1)]) # d c b a
```

### 字符串切片 slice 操作\_逆序

> 字符串切片规则可以用于其它序列
> 
> 切片 slice 操作可以让我们快速提取字符串，标准格式为：
> 
> **\[ 起始偏移量 start : 终止偏移量 end : 步长 step \]**
> 
> 

![PixPin\_2026\-07\-23\_21\-08\-05\.png](图片和附件/PixPin_2026-07-23_21-08-05.png)

![PixPin\_2026\-07\-23\_21\-10\-42\.png](图片和附件/PixPin_2026-07-23_21-10-42.png)

![PixPin\_2026\-07\-23\_21\-12\-46\.png](图片和附件/PixPin_2026-07-23_21-12-46.png)

```Python
str1 = "0123456789"

# 三个量为正数的情况
print(str1[:]) # 0123456789
print(str1[1:]) # 123456789
print(str1[:5]) # 01234
print(str1[2:5]) # 234
print(str1[1:8:2]) # 1357

# 三个量为负数的情况
print(str1[-3:]) # 789
print(str1[-8:-3]) # 23456
print(str1[-8:-3:2]) # 246
print(str1[::-1]) # 9876543210 反向提取，反转字符串
```

### split\(\)分割\_join合并\_代码效率测试

![PixPin\_2026\-07\-23\_21\-37\-39\.png](图片和附件/PixPin_2026-07-23_21-37-39.png)

![PixPin\_2026\-07\-23\_21\-38\-37\.png](图片和附件/PixPin_2026-07-23_21-38-37.png)

![PixPin\_2026\-07\-23\_21\-39\-02\.png](图片和附件/PixPin_2026-07-23_21-39-02.png)

> `join()` 是字符串对象的一个方法，用于将可迭代对象（如列表、元组、字符串等）中的元素用指定的分隔符连接成一个新的字符串。
> 
> 

```Python
# split()
# 字符串.split(分隔符)
str1 = "I love you"

print(str1.split()) # ['I', 'love', 'you']
print(str1.split('v')) # ['I lo', 'e you']

# join()
# 分隔符.join(可迭代对象)
str2 = "abc"
print("123".join(str2)) # a123b123c

str = "123"
print("abc".join(str)) # 1abc2abc3

lst = ["I", "love", "you"]
print("xx".join(lst)) # Ixxlovexxyou

yz = ("123", "456", "789")
print("yy".join(yz)) # 123yy456yy789
```

### **驻留机制\_同一判断\_值相等判断**

> 常量字符串只保留一份在内存中
> 
> 

```Python
a = "abcd_1234"
b = "abcd_1234"

print(a is b)  # True 比较地址
print(a == b)  # True 比较值
```

![PixPin\_2026\-07\-23\_22\-00\-57\.png](图片和附件/PixPin_2026-07-23_22-00-57.png)

![PixPin\_2026\-07\-23\_22\-01\-19\.png](图片和附件/PixPin_2026-07-23_22-01-19.png)

### **常用查找方法\_去除首尾信息\_大小写转换\_排版\_特征判断**

![PixPin\_2026\-07\-23\_22\-04\-40\.png](图片和附件/PixPin_2026-07-23_22-04-40.png)

![PixPin\_2026\-07\-23\_22\-11\-08\.png](图片和附件/PixPin_2026-07-23_22-11-08.png)

![PixPin\_2026\-07\-23\_22\-13\-54\.png](图片和附件/PixPin_2026-07-23_22-13-54.png)

![PixPin\_2026\-07\-23\_22\-15\-21\.png](图片和附件/PixPin_2026-07-23_22-15-21.png)

![PixPin\_2026\-07\-23\_22\-17\-30\.png](图片和附件/PixPin_2026-07-23_22-17-30.png)

![PixPin\_2026\-07\-23\_22\-19\-20\.png](图片和附件/PixPin_2026-07-23_22-19-20.png)

### 字符串格式化

![PixPin\_2026\-07\-23\_22\-31\-25\.png](图片和附件/PixPin_2026-07-23_22-31-25.png)

![PixPin\_2026\-07\-23\_22\-34\-02\.png](图片和附件/PixPin_2026-07-23_22-34-02.png)

![PixPin\_2026\-07\-23\_22\-35\-10\.png](图片和附件/PixPin_2026-07-23_22-35-10.png)

![PixPin\_2026\-07\-23\_22\-35\-49\.png](图片和附件/PixPin_2026-07-23_22-35-49.png)

### **可变字符串\_io\.StringIO**

> Python中，字符串属于不可变对象，**不支持原地修改**，如果需要修改其中的值，只能创建新的字符串对象。
> 
> 确实需要原地修改字符串，可以使用 io\.StringIO 对象或 array 模块
> 
> 

```Python
import io

s = "hello, xxx"
sio = io.StringIO(s) # sio 可变字符串, s 仍然是不可变的

print(sio)
v1 = sio.getvalue() # 获取字符串
print(v1) # hello, xxx
print(v1 is s) # False

ch = sio.seek(7) # 移动指针到第7个位置
print(ch) # 7

sio.write("yy") # 写入字符串
v2 = sio.getvalue() # 获取字符串
print(v2) # hello, yyx

print(s) # hello, xxx
```

## 类型转换总结

![PixPin\_2026\-07\-23\_23\-53\-30\.png](图片和附件/PixPin_2026-07-23_23-53-30.png)

![PixPin\_2026\-07\-23\_23\-55\-56\.png](图片和附件/PixPin_2026-07-23_23-55-56.png)

# 序列

![PixPin\_2026\-07\-24\_08\-43\-44\.png](图片和附件/PixPin_2026-07-24_08-43-44.png)

![PixPin\_2026\-07\-24\_08\-46\-30\.png](图片和附件/PixPin_2026-07-24_08-46-30.png)

> 注意：序列中每个数据都是离散在堆空间中的对象，序列本身不直接存放这些数据，而是将**这些对象的指针（引用）存放在一块连续的内存空间中。**
> 
> 

## 列表

### 简介

![PixPin\_2026\-07\-24\_08\-59\-42\.png](图片和附件/PixPin_2026-07-24_08-59-42.png)

![PixPin\_2026\-07\-24\_09\-01\-53\.png](图片和附件/PixPin_2026-07-24_09-01-53.png)

### 列表创建的四种方式

![PixPin\_2026\-07\-24\_21\-44\-13\.png](图片和附件/PixPin_2026-07-24_21-44-13.png)

![PixPin\_2026\-07\-24\_21\-47\-03\.png](图片和附件/PixPin_2026-07-24_21-47-03.png)

![PixPin\_2026\-07\-24\_21\-48\-34\.png](图片和附件/PixPin_2026-07-24_21-48-34.png)

```Python
r = range(6)
print(r) # range(0, 6)
print(type(r)) # <class 'range'> range 函数返回的是一个 range 对象，而不是一个列表。
print(list(r)) # [0, 1, 2, 3, 4, 5] 可以使用 list() 函数将 range 对象转换为列表。
```

### **元素的5种添加方式\_效率问题**

> 当列表增加和删除元素时，列表会自动进行内存管理，大大减少了程序员的负担。但这个特点涉及列表元素的大量移动，效率较低。 
> 
> 除非必要，我们一般只在列表的尾部添加元素或删除元素， 这会大大提高列表的操作效率。
> 
> 

![PixPin\_2026\-07\-24\_21\-58\-58\.png](图片和附件/PixPin_2026-07-24_21-58-58.png)

![PixPin\_2026\-07\-24\_22\-01\-47\.png](图片和附件/PixPin_2026-07-24_22-01-47.png)

![PixPin\_2026\-07\-24\_22\-04\-38\.png](图片和附件/PixPin_2026-07-24_22-04-38.png)

![PixPin\_2026\-07\-24\_22\-06\-16\.png](图片和附件/PixPin_2026-07-24_22-06-16.png)

![PixPin\_2026\-07\-24\_22\-07\-31\.png](图片和附件/PixPin_2026-07-24_22-07-31.png)

![PixPin\_2026\-07\-24\_22\-10\-04\.png](图片和附件/PixPin_2026-07-24_22-10-04.png)

### **列表删除的三种方式\_删除的本质是元素拷贝**

![PixPin\_2026\-07\-24\_22\-11\-35\.png](图片和附件/PixPin_2026-07-24_22-11-35.png)

![PixPin\_2026\-07\-24\_22\-12\-49\.png](图片和附件/PixPin_2026-07-24_22-12-49.png)

![PixPin\_2026\-07\-24\_22\-15\-08\.png](图片和附件/PixPin_2026-07-24_22-15-08.png)

```Python
b = [1, 2, 3, 4, 5]
print(b.pop(), b) # 5 [1, 2, 3, 4] 未指定索引删除最后一个元素

print(b.pop(1), b) # 2 [1, 3, 4] 指定索引删除元素
```

![PixPin\_2026\-07\-24\_22\-17\-47\.png](图片和附件/PixPin_2026-07-24_22-17-47.png)

### **元素的访问\_出现次数统计\_成员资格判断**

![PixPin\_2026\-07\-24\_22\-23\-09\.png](图片和附件/PixPin_2026-07-24_22-23-09.png)

```Python
a = [10, 20, 30, 40, 50, 50]
print(a.index(300)) # ValueError: list.index(x): x not in list
```

![PixPin\_2026\-07\-24\_22\-24\-41\.png](图片和附件/PixPin_2026-07-24_22-24-41.png)

![PixPin\_2026\-07\-24\_22\-25\-30\.png](图片和附件/PixPin_2026-07-24_22-25-30.png)

### 切片操作

![PixPin\_2026\-07\-24\_22\-29\-35\.png](图片和附件/PixPin_2026-07-24_22-29-35.png)

![PixPin\_2026\-07\-24\_22\-30\-29\.png](图片和附件/PixPin_2026-07-24_22-30-29.png)

![PixPin\_2026\-07\-24\_22\-32\-16\.png](图片和附件/PixPin_2026-07-24_22-32-16.png)

### **遍历\_排序\_max\_min\_sum**

![PixPin\_2026\-07\-24\_22\-37\-23\.png](图片和附件/PixPin_2026-07-24_22-37-23.png)

![PixPin\_2026\-07\-24\_22\-38\-09\.png](图片和附件/PixPin_2026-07-24_22-38-09.png)

![PixPin\_2026\-07\-24\_22\-39\-26\.png](图片和附件/PixPin_2026-07-24_22-39-26.png)

![PixPin\_2026\-07\-24\_22\-42\-02\.png](图片和附件/PixPin_2026-07-24_22-42-02.png)

![PixPin\_2026\-07\-24\_22\-43\-54\.png](图片和附件/PixPin_2026-07-24_22-43-54.png)

![PixPin\_2026\-07\-24\_22\-44\-33\.png](图片和附件/PixPin_2026-07-24_22-44-33.png)

### **二维列表\_表格数据存储和读取**

![PixPin\_2026\-07\-24\_22\-45\-20\.png](图片和附件/PixPin_2026-07-24_22-45-20.png)

![PixPin\_2026\-07\-24\_22\-46\-52\.png](图片和附件/PixPin_2026-07-24_22-46-52.png)

## 元组 tuple

![PixPin\_2026\-07\-25\_08\-34\-57\.png](图片和附件/PixPin_2026-07-25_08-34-57.png)

### **特点\_创建的两种方式\_tuple\(\)要点**

![PixPin\_2026\-07\-25\_08\-36\-24\.png](图片和附件/PixPin_2026-07-25_08-36-24.png)

```Python
a = 10, 20, 30
print(type(a)) # <class 'tuple'> 逗号分隔的多个值会被自动打包成一个元组。

b = (10)
print(type(b)) # <class 'int'> 只有一个值的元组需要在值后面加一个逗号。

c = (10, 20, 30)
print(type(c)) # <class 'tuple'> 逗号分隔的多个值会被自动打包成一个元组。

d = (10, )
print(type(d)) # <class 'tuple'> 只有一个值的元组需要在值后面加一个逗号。
```

![PixPin\_2026\-07\-25\_08\-39\-02\.png](图片和附件/PixPin_2026-07-25_08-39-02.png)

```Python
a = tuple(range(3))
print(a) # (0, 1, 2) range 函数返回的是一个 range 对象，而不是一个元组。可以使用 tuple() 函数将 range 对象转换为元组。

b = tuple([1, 2, 3])
print(b) # (1, 2, 3) 可以使用 tuple() 函数将列表转换为元组。

c = tuple(x for x in range(3))
print(c) # (0, 1, 2) 可以使用 tuple() 函数将生成器表达式转换为元组。

d = tuple("abc")
print(d) # ('a', 'b', 'c') 可以使用 tuple() 函数将字符串转换为元组。
```

### **元素访问\_计数方法\_切片操作\_成员资格判断\_zip\(\)**

![PixPin\_2026\-07\-25\_08\-50\-36\.png](图片和附件/PixPin_2026-07-25_08-50-36.png)

![PixPin\_2026\-07\-25\_08\-53\-04\.png](图片和附件/PixPin_2026-07-25_08-53-04.png)

> zip 函数只是把传入的可迭代对象转为元组，之后，可以用列表、元组等方式再外层接收打包的所有元组，形成多维。
> 
> 

```Python
a = [10, 20, 30]
b = [40, 50, 60]
c = [70, 80, 90, 100]
d = zip(a, b, c)
print(d, type(d)) # <zip object at 0x7f8c8c8c8c8c> zip 函数返回的是一个 zip 对象，而不是一个列表。可以使用 list() 函数将 zip 对象转换为列表。
print(tuple(d)) # ((10, 40, 70), (20, 50, 80), (30, 60, 90)) zip 函数将多个可迭代对象打包成一个元组的迭代器。可以使用 tuple() 函数将 zip 对象转换为元组。
print(list(d))  # [] zip 对象只能被迭代一次，迭代后就会被消耗掉。
```

```Python
x = zip(range(1, 3), "abc", [True, False, True])
print(list(x)) # [(1, 'a', True), (2, 'b', False)] zip 函数将多个可迭代对象打包成一个元组的迭代器。可以使用 list() 函数将 zip 对象转换为列表。
```

### 元组的删除

元组是不可变对象，不能删除元组中的元素，但是可以删除元组对象本身。

```Python
>>> tup = (1, 2, 3)
>>> del tup(1)  # 不能删除元组中的数据
  File "<stdin>", line 1
SyntaxError: cannot delete function call

>>> print(tup)
(1, 2, 3)

>>> del tup # 删除元组本身
>>> print(tup)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tup' is not defined
>>>
```

### **生成器推导式创建元组\_总结**

![PixPin\_2026\-07\-25\_09\-08\-26\.png](图片和附件/PixPin_2026-07-25_09-08-26.png)

```Python
a = (x**2 for x in range(3))
print(a, type(a)) # <generator object <genexpr> at 0x7f8c8c8c8c8c> 生成器表达式返回的是一个生成器对象，而不是一个元组。可以使用 tuple() 函数将生成器对象转换为元组。
print(tuple(a)) # (0, 1, 4) 可以使用 tuple() 函数将生成器对象转换为元组。
print(tuple(a)) # () 生成器对象只能被迭代一次，迭代后就会被消耗掉。

b = (x**2 for x in range(3))
print(b.__next__()) # 0 可以使用 __next__() 方法获取生成器对象的下一个值。
print(b.__next__()) # 1 可以使用 __next__() 方法获取生成器对象的下一个值。
print(b.__next__()) # 4 可以使用 __next__() 方法获取生成器对象的下一个值。
print(b.__next__()) # StopIteration ERROR 生成器对象只能被迭代一次，迭代后就会被消耗掉。
```

![PixPin\_2026\-07\-25\_09\-09\-36\.png](图片和附件/PixPin_2026-07-25_09-09-36.png)

## 字典

![PixPin\_2026\-07\-25\_09\-10\-49\.png](图片和附件/PixPin_2026-07-25_09-10-49.png)

![PixPin\_2026\-07\-25\_10\-01\-22\.png](图片和附件/PixPin_2026-07-25_10-01-22.png)

### 四种创建方式

1. 通过 \{\} 、dict\(\) 来创建字典对象

```Python
d1 = {"name": "张三", "age": 18, "gender": "男"}
print(d1)

d2 = dict(name="李四", age=20, gender="女")
print(d2)

d3 = dict([("name", "王五"), ("age", 22), ("gender", "男")])
print(d3)

d4 = {}
print(d4) # 空字典

d5 = dict()
print(d5) # 空字典
```

2. zip 函数创建字典对象

```Python
h = ["name", "age", "gender"]
b = ["张三", 18, "男"]
d6 = dict(zip(h, b))
print(d6) # {'name': '张三', 'age': 18, 'gender': '男'}
```

3. 通过 fromkeys 创建值为空的字典

```Python
f = dict.fromkeys(["name", "age", "gender"])
print(f) # {'name': None, 'age': None, 'gender': None}
```

### **元素的访问\_键的访问\_值的访问\_键值对的访问**

1. 通过 \[key\] 访问值，若键不存在，则抛出异常

```Python
d1 = {"name": "张三", "age": 18, "gender": "男"}
print(d1["name"]) # 张三 通过键获取值
print(d1["salary"]) # KeyError: 'salary' 如果键不存在，会抛出 KeyError 异常。
```

2. 通过 get\(\) 函数获取值，且推荐使用。

指定键如果不存在不会抛出异常，而是返回 None，或者可以指定不存在时返回什么。

```Python
d1 = {"name": "张三", "age": 18, "gender": "男"}

print(d1.get("age")) # 18
print(d1.get("salary")) # None 如果键不存在，get 方法会返回 None，而不是抛出异常。
print(d1.get("salary", 0)) # 0 如果键不存在，可以指定默认值。
```

3. 通过 items\(\) 函数列出所有的键值对

```Python
d1 = {"name": "张三", "age": 18, "gender": "男"}
print(d1.items()) # dict_items([('name', '张三'), ('age', 18), ('gender', '男')]) items 方法返回一个包含字典中所有键值对的视图对象。
```

4. 列出所有的键、列出所有的值

```Python
d1 = {"name": "张三", "age": 18, "gender": "男"}
print(d1.keys()) # dict_keys(['name', 'age', 'gender'])
print(d1.values()) # dict_values(['张三', 18, '男'])

# print(d1.keys()[0]) # TypeError: 'dict_keys' object is not subscriptable dict_keys 对象不支持索引操作。
print(list(d1.keys())[0]) # name 可以使用 list() 函数将 dict_keys 对象转换为列表，从而支持索引操作。
```

5. 获取键值对的个数 len\(\)

```Python
a = {'name':'gaoqi','age':18,'job':'programmer'} 
 num = len(a) 
 print(num)  #3 
```

6. 检测键是否在字典中 in、not in

```Python
d1 = {"name": "张三", "age": 18, "gender": "男"}

print("name" in d1)
print("salary" not in d1) # False 可以使用 in 运算符判断键是否存在于字典中。
```

### **元素的添加\_修改\_删除**

1. \[ key \] = val 

如果 key 存在，则覆盖旧值；不存在，则新增键值对。

```Python
a = {"name": "python"}
a["name"] = "js"
print(a) # {'name': 'js'} 通过键修改字典中的值。

a["age"] = 19
print(a) # {'name': 'js', 'age': 19} 通过键添加字典中的值。
```

2. update\(\) 函数

使用该函数将新字典中所有键值对全部添加到旧字典中，如果 key 有重复，则覆盖。

```Python
a = {'name':'gaoqi', 'age':18, 'job':'programmer'}
b = {'name':'gaoxixi','money':1000,'gender':'男的'}
a.update(b)
print(a) # {'name': 'gaoxixi', 'age': 18, 'job': 'programmer', 'money': 1000, 'gender': '男的'}
```

3. del\(\)、clear\(\)、pop\(\)

> del\(\) : 删除指定键值对对应的元素
> 
> clear\(\) : 清空字典元素
> 
> pop\(\) : 删除指定键值对，并返回对应的值对象
> 
> 

```Python
a = {'name':'gaoqi', 'age':18, 'job':'programmer', "qita": "gaoqi"}

del(a["name"])
print(a) # {'age': 18, 'job': 'programmer', 'qita': 'gaoqi'} 通过键删除字典中的值。

x = a.pop("age")
print(x) # 18 pop 方法会返回被删除的值。
print(a) # {'job': 'programmer', 'qita': 'gaoqi'} 通过 pop 方法删除字典中的值。

a.clear()
print(a) # {} clear 方法会清空字典中的所有键值对。
```

4. popitem\(\) 随即删除和返回该键值对

字典是“无序可变序列”， 因此没有第一个元素、最后一个元素的概念； popitem 弹出随机的项（返回被删除的键值对元组），因为字典并没有"最后的元素"或者其他有关顺序的概念。若想一个接一个地移除并处理项，这个方法就非常有效。

```Python
a = {'name':'gaoqi', 'age':18, 'job':'programmer'}
r = a.popitem()
print(r) # ('job', 'programmer') popitem 方法会随机删除字典中的一个键值对，并返回被删除的键值对。
print(a) # {'name': 'gaoqi', 'age': 18} pop
```

### **序列解包用于列表元组字典**

序列解包用于字典时，默认是对“键”进行操作； 如果需要对键值对操作，则需要使用items\(\)；如果需要对“值”进行操作，则需要使用 values\(\)；

![PixPin\_2026\-07\-25\_11\-37\-12\.png](图片和附件/PixPin_2026-07-25_11-37-12.png)

```Python
a = {"name": "python", "age": 18}
name, age = a*;*
print(name, age) # name age 可以使用字典解包将字典中的键赋值给多个变量。

name, age = a.items()
print(name, age) # ('name', 'python') ('age', 18)

name, age = a.values()
print(name, age) # python 18
```

### 复杂表格数据存储\_列表字典嵌套

```Python
r1 = {"name":"高小一", "age":18, "salary":30000, "city":"北京"}
r2 = {"name":"高小二", "age":19, "salary":20000, "city":"上海"}
r3 = {"name":"高小五", "age":20, "salary":10000, "city":"深圳"}
tb = [r1, r2, r3]

#获得第二行的人的薪资
print(tb[1].get("salary"))

#打印表中所有的的薪资
for i in range(len(tb)):   # i --> 0, 1, 2
    print(tb[i].get("salary"))

#打印表的所有数据
for i in range(len(tb)):
    print(tb[i].get("name"),tb[i].get("age"),
          tb[i].get("salary"),tb[i].get("city"))
```

### **核心底层原理\_内存分析\_存储键值对过程**

![PixPin\_2026\-07\-25\_12\-13\-47\.png](图片和附件/PixPin_2026-07-25_12-13-47.png)

![PixPin\_2026\-07\-25\_12\-19\-29\.png](图片和附件/PixPin_2026-07-25_12-19-29.png)

![PixPin\_2026\-07\-25\_12\-21\-01\.png](图片和附件/PixPin_2026-07-25_12-21-01.png)

```Python
print(bin(hash("name"))) # 0b101101000111001000001000110110100110111100101011100010111101000
```

### **核心底层原理\_内存分析\_查找值对象过程**

![PixPin\_2026\-07\-25\_12\-23\-02\.png](图片和附件/PixPin_2026-07-25_12-23-02.png)

![PixPin\_2026\-07\-25\_12\-24\-31\.png](图片和附件/PixPin_2026-07-25_12-24-31.png)

![PixPin\_2026\-07\-25\_12\-26\-29\.png](图片和附件/PixPin_2026-07-25_12-26-29.png)

## 集合

集合是**无序可变，元素不能重复的序列**。实际上，集合底层是字典实现， 集合的所有元素都是字典中的“键对象”，因此是**不能重复的且唯一的**。 

### 集合的创建和删除

![PixPin\_2026\-07\-25\_12\-34\-27\.png](图片和附件/PixPin_2026-07-25_12-34-27.png)

```Python
'''
1. remove(x) 删除指定的元素，如果元素不在集合中会报错
2. discard(x) 删除指定的元素，如果不存在不会报错
3. pop() 默认删除最后元素，可以返回得到删除的元素
'''
>>> st = {10, 20, 30}
>>> st.remove(40)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 40
>>> st.discard(40)
>>> print(st)
{10, 20, 30}
>>> x = st.pop()
>>> print(x)
10
```

```Python
s = {1, 2, 3} # 不能用 {} 定义空集合，会被认为是 dict

s.add(1)

print(s) # {1, 2, 3} set 不允许重复元素，因此添加重复元素不会改变集合的内容。
```

```Python
s = set("abc")
print(s) # {'a', 'b', 'c'} set 可以使用 set() 函数将字符串转换为集合。

s = set([1, 2, 3])
print(s) # {1, 2, 3} set 可以使用 set() 函数将列表转换为集合。

s = set({"name": "张三", "age": 18, "gender": "男"})
print(s) # {'name', 'age', 'gender'} set

s = set((1, 2, 3, 1))
print(s) # {1, 2, 3} set 可以使用 set() 函数将元组转换为集合。
```

### 集合操作

像数学中概念一样，Python对集合也提供了并集、交集、差集等运算。

```Python
# 集合的并集、交集、差集
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# 符号处理
print(s1 | s2) # {1, 2, 3, 4, 5} 并集
print(s1 & s2) # {3} 交集
print(s1 - s2) # {1, 2} 差集

# 函数处理
print(s1.union(s2)) # {1, 2, 3, 4, 5} 并集
print(s1.intersection(s2)) # {3} 交集
print(s1.difference(s2)) # {1, 2} 差集
```

## 序列总结

> - 可变 就是原地换内容，地址不变；不可变 就是换内容就得换新地址，旧对象不动。比如列表可变，使用 lst\[1\] = new\_val ，此时再获取 lst\[1\] 的 id 就不一样了。
> 
> 

```Python
# 1. 测试列表
lst = [10, 20]
print("列表修改前 id:", id(lst))  # 假设输出: 140000

lst.append(30) # 原地尾部追加
print("列表修改后 id:", id(lst))  # 依然输出: 140000 (id 完全没变！)
print("列表内容:", lst)           # [10, 20, 30]

# 2. 测试元组
tup = (10, 20)
print("元组修改前 id:", id(tup))  # 假设输出: 160000

# 元组不能 append，只能通过拼接创建一个新的元组
tup = tup + (30,)
print("元组修改后 id:", id(tup))  # 输出变为了一个新地址，例如 170000 (id 变了！)
print("元组内容:", tup)           # (10, 20, 30)
```

|特性分类|列表 \(List\)|元组 \(Tuple\)|字符串 \(String\)|字典 \(Dictionary\)|集合 \(Set\)|
|---|---|---|---|---|---|
|符号/表示|`[10, 20, 30]`|`(10, 20, 30)` 或 `10, 20`|`"hello"` 或 `'hello'`|`{"key":"value"}`|`{10, 20, 30}`|
|可变性|✅ 可变 \(可增删改\)|❌ 不可变|❌ 不可变|✅ 可变|✅ 可变|
|有序性|✅ 有序 \(有索引\)|✅ 有序 \(有索引\)|✅ 有序 \(有索引\)|✅ 有序 \(3\.7\+ 保留插入顺序\)|❌ 无序 \(无索引\)|
|元素重复性|允许重复|允许重复|允许重复|键不允许重复，值可重复|元素不允许重复|
|元素类型要求|任意类型，混合均可|任意类型，混合均可|必须是字符 \(Char\)|键必须是不可变类型\(如数字、字符串、元组\)；值可为任意类型|元素必须是不可变类型<br>|
|创建方式|`[]`, `list()`, `list(range())`, 推导式|`()`, `tuple()`, 单元素需加逗号 `(1,)`|`""`, `str()`, `''`|`{}`, `dict()`, `zip()` 生成, `fromkeys`|`set()`, `set(可迭代对象)`<br>*\(注意：**`{}`** 默认为空字典\)*|
|访问方式|索引 `a[0]`，切片 `a[0:3]`|索引 `a[0]`，切片 `a[0:3]`|索引 `a[0]`，切片 `a[0:3]`|键访问 `a["name"]`，`.get()`|无法通过索引/键访问，只能判断“是否在其中” \(in\)|
|常用方法|`append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`|`index()`, `count()`, `len()`|`split()`, `join()`, `replace()`, `find()`|`.keys()`, `.values()`, `.items()`, `.get()`, `.pop()`, `.update()`|`.add()`, `.remove()`, `|`\(并\), `&`\(交\), `-`\(差\)|
|底层实现|连续内存空间，存放对象地址的数组|连续内存空间，存放对象地址的数组|连续内存空间，存放字符编码|哈希表 \(散列表\) \(稀疏数组，由 bucket 组成\)|哈希表 \(底层实为字典，仅存储键，值是空\)|
|性能/注意点|尾部增删极快，中间插入/删除极慢|读取速度比列表快，可作为字典的键|不可修改，所有操作均返回新字符串|查询速度极快，但内存占用极大 \(空间换时间\)|常用于数据去重和集合数学运算|

# 控制语句

## 控制语句和现实逻辑表达

> - 顺序结构：先执行 a，再执行 b \.\.\.\.\.\.
> 
> - 条件判断结构：如果 \.\.\. 则 \.\.\.
> 
> - 循环结构：如果 \.\.\. 则重复执行
> 
> 

## 条件判断结构（选择结构）

选择结构通过判断条件是否成立，来决定执行哪个分支。选择结构 有多种形式，分为：**单分支、双分支、多分支**。

### **单分支选择结构\_条件表达式详解**

> **if 条件表达式:  **
> 
> **语句/语句块**
> 
> 
> 
> - 条件表达式：可以是逻辑表达式、关系表达式、算术表达式等等。 
> 
> - 语句/语句块：可以是一条语句，也可以是多条语句。**多条语句，缩进必须对齐一致**
> 
> 

在选择和循环结构中，条件表达式的值为 False 的情况如下： **False、0、0\.0、空值None、空序列对象（空列表、空元祖、 空集合、空字典、空字符 串）、空range对象、空迭代对象**。 其他情况，均为 True 。这么看来，Python所有的合法表达式都可以看做条件表达式，甚至包括函数调用的表达式。

```Python
i = 5

if 3 < i < 9:
    print("i 的值在 3 和 9 之间") # i 的值在 3 和 9 之间
```

> **条件表达式中，不能有赋值操作符 =** 
> 
> 在Python中，条件表达式不能出现赋值操作符 = ，避免了其他语言中经常误将关系运算符 == 写作赋值运算符 = 带来的困扰。
> 
> 

```Python
i = 5
j = 100
if j > 0 and (i = 0):  # SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
    print("test")
```

### 双分支选择结构和三元运算符

> if 条件表达式:  
> 
> 语句1/语句块1 
> 
> else:  
> 
> 语句2/语句块2
> 
> 

![PixPin\_2026\-07\-25\_15\-46\-56\.png](图片和附件/PixPin_2026-07-25_15-46-56.png)

```Python
num = -3

# 三元运算符用来在某些简单双分支赋值情况
print(num if num > 0 else -num) # 3 三元运算符，判断 num 是否大于 0，如果是则返回 num，否则返回 -num。
```

### 多分支选择结构

> if 条件表达式1 :  
> 
> 语句1/语句块1 
> 
> elif 条件表达式2:    \# elif 后面必须携带条件表达式，else 则必须不能携带
> 
> 语句2/语句块2 \.\.\. 
> 
> elif 条件表达式n :  
> 
> 语句n/语句块n 
> 
> \[else:   \# 非必须使用
> 
> 语句n\+1/语句块n\+1 
> 
> \] 
> 
> 

```Python
score = int(input("请输入分数"))
grade = ''

if(score < 60):
    grade = "不及格"
if(60 <= score < 80):
    grade = "及格"
if(80 <= score < 90):
    grade = "良好"
if(90 <= score <= 100):
    grade = "优秀"

print("分数是{0},等级是{1}".format(score, grade))

# 改成多分支结构
if score < 60 :
    grade = "不及格"
elif score < 80 :
    grade = "及格"
elif score < 90 :
    grade = "良好"
elif score <= 100:
    grade = "优秀"
```

### 选择嵌套

选择结构可以嵌套，使用时一定要注意控制好不同级别代码块的缩 进量，因为**缩进量决定了代码的从属关系**。

![PixPin\_2026\-07\-25\_16\-00\-28\.png](图片和附件/PixPin_2026-07-25_16-00-28.png)

## 循环结构

### while 循环结构

> while 条件表达式：  
> 
> 循环体
> 
> 

```Python
num, sum_num = 0, 0

while num <= 100:
    sum_num += num
    num += 1

print("1-100的和是：", sum_num)
```

### for 循环结构和可迭代对象遍历

> **for 循环通常用于可迭代对象的遍历**
> 
> for  变量  in  可迭代对象：  
> 
> 循环体
> 
> 

![PixPin\_2026\-07\-25\_16\-20\-38\.png](图片和附件/PixPin_2026-07-25_16-20-38.png)

![PixPin\_2026\-07\-25\_16\-24\-59\.png](图片和附件/PixPin_2026-07-25_16-24-59.png)

```Python
# 1、遍历 range 可迭代对象
num, sum_num = 0, 0
for i in range(1, 101, 1):
    sum_num += i

print("1-100的和是：", sum_num)

# 2、遍历字典
students = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 22},
    {"name": "Charlie", "age": 21}
]

for s in students:
    print(s.get("name"), s.get("age"))
```

```Python
# 9 * 9 乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{0} * {1} = {2}".format(i, j, i * j), end="\t")
    print()
```

### break 语句

break语句可用于while和for循环，**用来结束整个循环**。当有嵌套循环时，break语句只能跳出最近一层的循环。

```Python
while True:
    a = input("请输入一个字符（输入Q或q结束）")
    if a.upper()=='Q':
        print("循环结束，退出")
        break
    else:
        print(a)
```

### continue 语句

continue语句用于**结束本次循环，继续下一次**。多个循环嵌套时，continue也是应用于最近的一层循环。 

```Python
sum_num = 0
for x in (10, 20, -30, 90, -100):
    if x < 0:
        continue

    sum_num += x

print("正数的和是：", sum_num) # 120
```

### else 语句

**while、for循环可以附带一个else语句（可选）**。如果for、while语句**没有被break语句结束，则会执行else子句，否则不执行**。

```Python
# 也就是如果循环是因为 break 被结束的就不会进入 else 代码块
while 条件表达式：  
    循环体 
else:  
    语句块 
    
或者： 

for 变量 in 可迭代对象：  
    循环体 
else:  
    语句块
```

### 循环代码优化

虽然计算机越来越快，空间也越来越大，我们仍然要在性能问题上 “斤斤计较”。编写循环时，遵守下面三个原则可以大大提高运行效率，避免不必要的低效计算：

> - 尽量减少循环内部不必要的计算 
> 
> - 嵌套循环中，尽量减少内层循环的计算，尽可能向外提 
> 
> - 局部变量查询较快，尽量使用局部变量
> 
> 

### 使用 zip 并行迭代多个序列

可以通过zip\(\)函数对多个序列进行并行迭代，zip\(\)函数在最短序列“用完”时就会停止。

```Python
names = ("高淇", "高老二", "高老三", "高老四")
ages = (18, 16, 20, 25)
jobs = ("老师", "程序员", "公务员")

# zip
for name, age, job in zip(names, ages, jobs):
    print("{0}的年龄是{1}，职业是{2}".format(name, age, job))

for i in range(min(len(names), len(ages), len(jobs))):
    print("{0}的年龄是{1}，职业是{2}".format(names[i], ages[i], jobs[i]))
```

## 推导式创建序列

推导式是**从一个或者多个迭代器快速创建序列**的一种方法。它可以**将循环和条件判断结合**，从而**避免冗长代码**。推导式是典型的Python风格。

### 列表推导式

```Python
[表达式 for item in 可迭代对象]
或者：
{表达式 for item in 可迭代对象 if 条件判断}
```

```Python
und = [ord(c) for c in "Hello, World!" if c.isalpha()]
print(und) # [72, 101, 108, 108, 111]
```

### 字典推导式

```Python
# 类似于列表推导式，字典推导也可以增加if条件判断、多个for循环。
{key_expression : value_expression for 表达式 in 可迭代对象}
```

```Python
values = ["北京", "上海", "深圳", "广州"]
cities = {id * 100 : city for id, city in zip(range(1,5), values)}
print(cities) # {100: '北京', 200: '上海', 300: '深圳', 400: '广州'}
```

```Python
txt = "I have a dream that one day this nation will rise up and live out the true meaning of \
    its creed: 'We hold these truths to be self-evident, that all men are created equal.'"

# 统计字母的数量
cnt = {word : txt.count(word) for word in txt if word.isalpha()}
print(cnt)
```

### 集合推导式

```Python
{表达式 for item in 可迭代对象 } 
或者：
{表达式 for item in 可迭代对象 if 条件 判断} 
```

```Python
s = {x ** 2 for x in range(4) if x % 2 == 0}
print(s) # {0, 4}
```

### 生成器推导式（不直接生成元组）

一个生成器只能运行一次。第一次迭代可以得到数据，第二次迭代发现数据已经没有了。

```Python
gnt = (x for x in range(4) if x % 2 == 0)
print(gnt) # <generator object <genexpr> at 0x0000013423FF8FB0>

# tuple(gnt) 转为元组
# list(gnt) 转为列表

for x in gnt:
    print(x) # 0 2
```

# 函数和内存分析

> - 函数是可重用的代码块
> 
> - 函数作用：不仅可以实现代码的**复用**，更能实现代码的**一致性**。一致性指的是只要修改函数的代码，则所有调用该函数的地方都能得到体现。 
> 
> 

![PixPin\_2026\-07\-26\_22\-14\-14\.png](图片和附件/PixPin_2026-07-26_22-14-14.png)

## 函数简介

1. 基本概念

> 1. 一个程序由一个一个的任务组成；函数就是代表一个任务或者一个功能\(function\)。 
> 
> 2. 函数是代码复用的通用机制 。
> 
> 

2. 函数分类

> - 内置函数：可以直接拿来用，比如 str\(\)、len\(\)、list\(\)、tuple\(\) 等。
> 
> - 标准库函数：通过 import 语句导入库，然后才能使用其中的函数。
> 
> - 第三方库函数：下载他人发布的库，然后使用 import 导入，即可使用。
> 
> - 用户自定义函数：自己开发的适用自己需求的函数。
> 
> 

3. 函数的定义和调用

```Python
# 函数定义语法
def  函数名 ([参数列表]):
    '''文档字符串(说明函数，可选但推荐)'''
    函数体/若干语句

# 求两数之和
def my_sum(x, y):
    return x + y
```

> **要点**
> 
> 1. 使用 **def **来定义函数，然后跟随一个空格和函数名称（会创建一个函数对象，并绑定到函数名变量上）
> 
> 2. **参数列表：**
> 
>     1. 圆括号内是形式参数列表，多个参数则使用逗号隔开
> 
>     2. 定义时的形式参数不需要声明类型，也不需要指定函数返回值类型
> 
>     3. 调用时的实际参数必须与形式参数列表一一对应
> 
> 3. return 返回值
> 
>     1. 如果函数体中包含 return 语句，则结束函数执行并返回值
> 
>     2. 如果函数体中不包含 return 语句，则**默认返回 None 值**
> 
> 4. 调用函数之前，必须要先定义函数，即使用 def 创建函数对象
> 
>     1. 内置函数对象会自动创建
> 
>     2. 标准库和第三方库函数，通过 import 导入模块时，会执行模块中的 def 语句
> 
> 

## 形参和实参\_文档字符串\_函数注释

### 形参和实参要点

> - 圆括号内是形式参数列表，有多个参数则使用逗号隔开
> 
> - 定义时的形式参数不需要声明类型，也不需要指定函数返回值类型
> 
> - 调用时的实际参数必须与形参列表一一对应 
> 
> 

```Python
def compute(start, end):
    total = 0
    for i in range(start, end + 1, 1):
        total += i

    return total

result = compute(1, 10) # 1, 10 为实参
print(result)
```

### 文档字符串（函数的注释）

> - 程序的可读性最重要，一般建议在函数体开始的部分附上函数定义说明，这就是“文档字符串”，也有人成为“函数的注释”。
> 
> - **通过三个单引号或者三个双引号来实现**，中间可以加入多行文字进行说明。 
> 
> - 通过函数名可以获取文档字符串，以了解函数的功能。
> 
> 

```Python
def compute(start, end):
    '''
    计算指定范围的累加和
    :param start: 起始值
    :param end: 结束值
    :return: 累加和
    '''
    total = 0
    for i in range(start, end + 1, 1):
        total += i

    return total

# 方法一：通过这个 help 函数可以获取到这个函数的说明文档
help(compute)

# 方法二：函数的 __doc__ 属性可以获取到这个函数的说明文档
print(compute.__doc__)

# 输出：
计算指定范围的累加和
:param start: 起始值
:param end: 结束值
:return: 累加和
```

## 返回值

> - 如果函数体中包含 return 语句，则结束函数执行并返回值
> 
> - 如果函数体中不包含 return 语句，则默认返回 None 值
> 
> - 要返回多个值，使用列表、元组、字典、集合将多个值“存起来”即可 
> 
> 

```Python
def return_tup():
    tup = (1, 2, 3, 4, 5)
    return tup
    
    
def return_none():
    pass  # 给函数占位

print(return_none() ) # None
```

## 函数对象内存分析

函数也是对象。

```Python
def print_star(n):
    print("*" * n)

print(print_star) # <function print_star at 0x0000000002BB8620>
print(id(print_star)) # 45844000

c = print_star # 和 print_star 指向同一个对象
print(c) # <function c at 0x0000000002BB8620>
print(id(c)) # 45844000
```

![PixPin\_2026\-07\-26\_22\-58\-54\.png](图片和附件/PixPin_2026-07-26_22-58-54.png)

## 变量的作用域（全局变量和局部变量）

1. 全局变量

> - 在函数和类定义之外声明的变量。作用域为定义的模块，从定义位置开始直到模块结束。 
> 
> - 全局变量降低了函数的通用性和可读性。应**尽量避免全局变量的使用**。
> 
> - 要在函数内改变全局变量的值，使用 **global **声明一下
> 
> 

2. 局部变量

> - 在函数体中（包含形式参数）声明的变量。
> 
> - 局部变量的引用比全局变量快，优先考虑使用
> 
> - 如果局部变量和全局变量同名，则在**函数内隐藏全局变量，只使用同名的局部变量**
> 
> 

```Python
a = 10
def t1(x):
    print(x) # 9
    a = 100
    print(a) # 100

t1(9)
print(a) # 10 函数内的 a = 100 是局部变量，函数外的 a = 10 是全局变量
```

```Python
a = 10
def t1(x):
    print(x) # 9
    global a # 声明 a 是全局变量
    a = 100
    print(a) # 100

t1(9)
print(a) # 100 函数内的 a = 100 是局部变量，函数外的 a = 100 是全局变量
```

```Python
a = 10
def t1(x):
    print(x) # 9
    print(locals()) # locals() 函数可以获取到函数内的局部变量
    print(globals()) # globals() 函数可以获取到函数外的全局变量

t1(9)

# 输出
9
{'x': 9}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000026C03CD71D0>, '__spec__': None, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'd:\\python\\py_project\\pro1\\demo26.py', '__cached__': None, 'a': 10, 't1': <function t1 at 0x0000026C03D9F8A0>}
```

## 全局变量和局部变量效率测试

> - `LOAD_FAST`（局部）：变量存储在栈帧（frame）的 `f_localsplus` 数组中，通过整数索引直接偏移读取，等价于 C 语言中的数组取值，极快。
> 
> - `LOAD_GLOBAL`（全局）：需要先查找模块的 `dict` 字典（哈希表），如果找不到还要去 `builtins` 模块里找。哈希查找涉及计算哈希值、处理冲突、比较键值，而且全局字典是动态可变的，无法像数组那样做编译期优化。
> 
> 

```Python
import time

num = 0

def add_global():
    global num

    start = int(time.time())
    for i in range(1, 100000000):
        num += i

    end = int(time.time())
    print("使用全局变量累加耗时 = {0}".format(end - start)) # 使用了 3 seconds
    return num

def add_local():
    num = 0
    start = int(time.time())
    for i in range(1, 100000000):
        num += i

    end = int(time.time())
    print("使用局部变量累加耗时 = {0}".format(end - start)) # 使用了 2 seconds
    return num

add_global()
add_local()
```

## 参数传递\_**传递可变/不可变对象\_内存分析**

> - Python 中一切皆对象，赋值操作都是 **“引用的赋值”**
> 
> - 函数的参数传递的本质上就是：从实参到形参的赋值操作。
> 
> - 所以，python 中参数的传递都是 “引用传递”，而不是 “值传递”
> 
> 

- 可变对象和不可变对象的传递

![PixPin\_2026\-07\-27\_08\-41\-32\.png](图片和附件/PixPin_2026-07-27_08-41-32.png)

- 可变对象的传递

> 传递参数是可变对象（例如：列表、字典、自定义的其他可变对象 等），实际传递的还是对象的引用。在函数体中**不创建新的对象拷贝，而是可以直接修改所传递的对象**。
> 
> 

![PixPin\_2026\-07\-27\_08\-45\-42\.png](图片和附件/PixPin_2026-07-27_08-45-42.png)

- 不可变对象的传递

> 传递参数是不可变对象（例如： int 、 float 、字符串、元组、布尔值），实际传递的还是对象的引用。在”赋值操作”时，由于**不可变对象无法修改，系统会新创建一个对象**。
> 
> 

```Python
tup1 = (1, 2, 'a') # 不可变对象
print(id(tup1), tup1)

'''
无论传递可变还是不可变对象，传递的都是对象的引用，所以
1、传进来的时候对象都是一样的，指向的都是同一个对象
2、区别其实是在函数中对对象有没有做写操作或者赋值操作
3、如果做了写操作或者赋值操作，不可变对象会创建新的对象
4、如果只是读取，不会新建对象，也不会影响原对象
'''
def test2(tup):
    print(id(tup), tup, tup is tup1) # 2016930826576 (1, 2, 'a') True
    tup += (4,)
    print(id(tup), tup) # 对象发生改变，2016931061072 (1, 2, 'a', 4)

test2(tup1)
print(id(tup1), tup1) # 2016930826576 (1, 2, 'a')
```

## 浅拷贝与深拷贝

![PixPin\_2026\-07\-27\_21\-48\-43\.png](图片和附件/PixPin_2026-07-27_21-48-43.png)

> 1. 浅拷贝：拷贝对象，但不拷贝子对象的内容，只是拷贝子对象的引用。对子对象的修改会影响到源对象。
> 
> 2. 深拷贝：拷贝对象，并且会连子对象的内存也全拷贝一份（递归拷贝一份），对子对象的修改不会影响源对象。
> 
> 3. copy 和 deepcopy 标准库函数可以实现浅拷贝和深拷贝。需要引入 copy 模块。
> 
> 

```Python
import copy

# 1、测试浅拷贝
def test_copy():
    lst1 = [1, 2, ['a', 'b']]
    print(id(lst1), "lst1 =", lst1) # 1576641345472 lst1 = [1, 2, ['a', 'b']]
    print(id(lst1[2]), "lst1[2] =", lst1[2]) # 1576641228736 lst1[2] = ['a', 'b']

    # 浅拷贝
    lst2 = copy.copy(lst1)
    lst2[2].append('c')

    print(id(lst1), "lst1 =", lst1) # 1576641345472 lst1 = [1, 2, ['a', 'b', 'c']]
    print(id(lst1[2]), "lst1[2] =", lst1[2]) # 1576641228736 lst1[2] = ['a', 'b', 'c']
    print(id(lst2), "lst2 =", lst2) # 1576642785792 lst2 = [1, 2, ['a', 'b', 'c']]
    print(id(lst2[2]), "lst2[2] =", lst2[2]) # 1576641228736 lst2[2] = ['a', 'b', 'c']

test_copy()
```

```Python
## 2、测试深拷贝
def test_deepcopy():
    lst1 = [1, 2, ['a', 'b']]
    print(id(lst1), "lst1 =", lst1) # 2507532515264 lst1 = [1, 2, ['a', 'b']]
    print(id(lst1[2]), "lst1[2] =", lst1[2]) # 2507532398528 lst1[2] = ['a', 'b']

    # 深拷贝
    lst2 = copy.deepcopy(lst1)
    lst2[2].append('c')

    print(id(lst1), "lst1 =", lst1) # 2507532515264 lst1 = [1, 2, ['a', 'b']]
    print(id(lst1[2]), "lst1[2] =", lst1[2]) # 2507532398528 lst1[2] = ['a', 'b']
    print(id(lst2), "lst2 =", lst2) # 2507534086400 lst2 = [1, 2, ['a', 'b', 'c']]
    print(id(lst2[2]), "lst2[2] =", lst2[2]) # 2507533612800 lst2[2] = ['a', 'b', 'c']

test_deepcopy()
```

## **不可变对象含可变子对象\_内存分析**

传递不可变对象时，不可变对象里包含的可变对象是可变的，函数内修改了这个对象，源对象也会修改。也就是说，这里是一个浅拷贝。

```Python
tup = (1, 2, ['a', 'b'])
print(id(tup), tup) # 2294011988144 (1, 2, ['a', 'b'])

def test(tp):
    print(id(tp), tp, tp is tup) # 2294011988144 (1, 2, ['a', 'b']) True
    tp[2].append('c')
    print(id(tp), tp, tp is tup) # 2294011988144 (1, 2, ['a', 'b', 'c']) True

print(id(tup), tup) # 2294011988144 (1, 2, ['a', 'b', 'c']) True
test(tup)
```

## **参数的类型**

- 参数的几种类型

![PixPin\_2026\-07\-27\_22\-18\-49\.png](图片和附件/PixPin_2026-07-27_22-18-49.png)

### 位置参数

函数调用时，实参默认按位置顺序传递，需要逐个与形参匹配，不能随意交换顺序。即按位置传递的参数称为 “位置参数”。

```Python
def f1(a, b, c):
    print(a, b, c)

f1(2, 3, 4)
f1(2, 3)     # TypeError: f1() missing 1 required positional argument: 'c
```

### 默认值参数

可以为某些参数设置默认值，这样这些参数在传递时就是**可选的**。称为“默认值参数”。默认值参数放到位置参数后面。

```Python
def f1(a, b, c=10, d=20):   # 默认值参数必须位于普通位置参数后面
    print(a, b, c, d)

f1(8, 9) # 8 9 10 20
f1(8, 9, 19) # 8 9 19 20
f1(8, 9, 19, 29) # 8 9 19 29
```

### 命名参数

可以按照形参的名称传递参数，称为“命名参数”，也称“关键字参数”。 此时，在调用函数的时候可以随意打算传递的顺序。

```Python
def f1(a, b, c):
    print(a, b, c)

f1(8, 9, 19)          # 位置参数  8 9 19
f1(c = 10, a = 20, b = 30)  # 命名参数  20 30 10
```

### 可变参数

可变参数指的是 “可变数量的参数”。分两种情况：

- \`\*param\` ：将多个参数收集到一个元组对象中

- \`\*\*param\` ：将多个参数收集到一个字典中

```Python
def f1(a, b, *c):
    print(a, b, c)

f1(8, 9, 19, 20) # 8 9 (19, 20)

def f2(a, b, **c):
    print(a, b, c)

# 对于 **param 参数，必须是 key = value 的传值格式，否则会报错。
# 所以 *param 和 **param 混用也不会报错
f2(8, 9, name = 'gaoqi', age = 18) # 8 9 {'name': 'gaoqi', 'age': 18}

def f3(a, b, *c, **d):
    print(a, b, c, d)

f3(8, 9, 20, 30, name = 'gaoqi', age = 18) # 8 9 (20, 30) {'name': 'gaoqi', 'age': 18}
```

### 强制命名参数

在带星号的“可变参数”后面增加新的参数，必须在调用的时候“强制命名参数”。

所以这种参数类型是为了解决 可变参数可以放在任意位置的问题。 

```Python
def f1(*a, b, c):
    print(a, b, c)

f1(10, 20, 30, c = 40, b = 50) # (10, 20, 30) 50 40
f1(10, 20, 30, 40, 50) # TypeError: f1() missing 2 required keyword-only arguments: 'b' and 'c'
```

## Lambda 表达式和匿名函数

- lambda 表达式可以用来声明匿名函数。 lambda 函数是一种简单的、在同一行中定义函数的方法。 

- lambda 函数实际生成了一个函数对象。 

- lambda 表达式**只允许包含一个表达式，不能包含复杂语句**，该表达式的计算结果就是函数的返回值。

- 基本语法：lambda arg1, arg2, \.\.\. : \<表达式\>

```Python
f = lambda a, b : a if a > b else b
print(f) # <function <lambda> at 0x000001384B90F8A0>
print(id(f)) # 1341297588384
print(type(f)) # <class 'function'>
print(f(10, 20)) # 20

g = [lambda a : a ** 2, lambda a : a ** 3, lambda a : a ** 4]
print(g) # [<function <lambda> at 0x000001384B90F9D0>, <function <lambda> at 0x000001384B90FA60>, <function <lambda> at 0x000001384B90FAF0>]
print(g[0](2)) # 4
print(g[1](2)) # 8
print(g[2](2)) # 16
```

## eval 函数和注入风险

将字符串 str 当成有效的表达式来求值并返回计算结果。

语法：eval\(source\[, globals\[, locals\]\]\) \-\> value

- source : 一个 python 表达式

- globals : 可选，必须是 dictionary

- locals : 可选，任意映射对象

```Python
s1 = "print('hello')"
eval(s1) # hello

a, b = 10, 20
c = eval("a + b")
print(c) # 30

x = eval("a ** 3 + int('123') + b", {"a": 10, "b": 20})
print(x) # 1143
```

eval函数会将字符串当做语句来执行，因此会被注入安全隐患。比如：字符串中含有删除文件的语句。

## 递归函数

```Python

def feibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return feibonacci(n - 1) + feibonacci(n - 2)

print(feibonacci(10)) # 55
```

## 嵌套函数（内部函数）

嵌套函数是在函数内部定义的函数。

```Python
# inner() 就是定义在 outer() 函数内部的函数。 
# inner() 的定义和调用都在 outer() 函数内部。
def  outer():
    print('outer running...')

    def inner():
        print('inner running...')

    inner()

outer()

# outer running... 
# inner running...
```

- 嵌套函数使用的情况

> 1. 封装 \- 数据隐藏 外部无法访问“嵌套函数”
> 
> 2. 贯彻 DRY\(Don’t Repeat Yourself\) 原则 3
> 
> 3. 嵌套函数，可以让我们在函数内部避免重复代码
> 
> 4. 闭包
> 
> 

![PixPin\_2026\-07\-28\_08\-19\-07\.png](图片和附件/PixPin_2026-07-28_08-19-07.png)

## nonlocal 关键字

![PixPin\_2026\-07\-28\_08\-20\-18\.png](图片和附件/PixPin_2026-07-28_08-20-18.png)

> - nonlocal 用来在内部函数中，声明外层的局部变量。
> 
> - global 函数内声明全局变量，然后才使用全局变量。
> 
> 

> - 无论 `global` 还是 `nonlocal`，只要不给变量名“穿新衣服”（即不用 `=`、`+=`、`*=` 等赋值运算符），只是拿着现有的东西“倒腾内部”（如 `.append()`、`.remove()`、`dict.update()`），就不需要 `nonlocal`，他们的修改也是会作用到外部的变量。
> 
> 

```Python
# 测试nonlocal、global关键字的用法
a = 100
def outer():
    b = 10
    def inner():
        nonlocal  b         # 声明外部函数的局部变量
        print("inner b:",b) # inner b: 10

        b = 20

        global a            # 声明全局变量
        a = 1000

    inner()
    print("outer b:",b) # outer b: 20

outer()
print("a =",a) # a = 1000
```

```Python
def  outer():
    lst = [100, 200, 300]

    def inner():
        lst.append(400)
        print('inner running...')
        print(lst) # [100, 200, 300, 400]

    inner()
    print(lst) # [100, 200, 300, 400] 被内部函数修改了

outer()
```

## LEGB 变量搜索规则

![PixPin\_2026\-07\-28\_08\-40\-25\.png](图片和附件/PixPin_2026-07-28_08-40-25.png)

> - Local 指的就是函数或者类的方法内部
> 
> - Enclosed 指的是嵌套函数（一个函数包裹另一个函数，闭包）
> 
> - Global 指的是模块中的全局变量
> 
> - Built in 指的是Python为自己保留的特殊名称
> 
> 如果某个 name 映射在局部 local 命名空间中没有找到，接下来就会在闭包作用域 enclosed 进行搜索，如果闭包作用域也没有找到， Python就会到全局 global 命名空间中进行查找，最后会在内建 built\-in 命名空间搜索 （如果一个名称在所有命名空间中都没有找 到，就会产生一个 NameError ）
> 
> 

```Python
# 测试 LEGB
s = "global"
def outer():
    s = "outer"

    def inner():
        s = "inner"
        print(s)

    inner() # inner

outer()
```

## 练习

```Python
def reserve_num(num):
    '''
    反转数字
    :param num: 需要反转的数字
    :return: 反转后的数字
    '''
    sign = -1 if num < 0 else 1
    num = abs(num)
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num //= 10

    return result * sign

print(reserve_num(-123)) # -321
```

```Python
def compute(n):
    '''
    m(n) = 1 / 2 + 2 / 3 + 3 / 4 + ... + n / (n + 1)
    '''
    result = 0

    if (n == 1):
        return 1 / (n + 1)

    return result + n / (n + 1) + compute(n - 1)

print(compute(2))
```

# 面向对象

![PixPin\_2026\-07\-29\_22\-38\-38\.png](图片和附件/PixPin_2026-07-29_22-38-38.png)

## **面向对象和面向过程的区别\_设计者思维\_执行者思维**

![PixPin\_2026\-07\-29\_22\-49\-53\.png](图片和附件/PixPin_2026-07-29_22-49-53.png)

## 对象进化

处理越来越复杂。

![PixPin\_2026\-07\-30\_08\-38\-11\.png](图片和附件/PixPin_2026-07-30_08-38-11.png)

## **类的定义\_类和对象的关系\_对象的内存模型**

- 类的定义

> 类：class 。 定义属性和方法的模板。
> 
> 对象：object , instance \(实例\)。是一个意思。具体的实例，承载实际数据。
> 
> 

- 属性和方法

类可以将状态和行为打包在一起。

```Python
# 语法格式
class 类名:
    类体
    
# 要点
# 1、类名必须符合“标识符”的规则；一般规定，首字母大写，多个单词使用“驼峰原则”。 
# 2、类体中我们可以定义属性和方法 
# 3、属性用来描述数据，方法(即函数)用来描述这些数据相关的操作
```

Python 中，”一切皆对象“。类也称为”类对象“，类的实例也称为”实例对象“。

![PixPin\_2026\-07\-30\_08\-44\-42\.png](图片和附件/PixPin_2026-07-30_08-44-42.png)

> `pass `为空语句。就是**表示什么都不做，只是作为一个占位符存在**。当你写代码时，遇到暂时不知道往方法或者类中加入什么 时，可以先用pass占位，后期再补上。
> 
> 

```Python
class Student:
    # __init__ 构造方法，第一个参数必须是 self，可以改为其它自定义名称
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def take_exam(self, subject):
        pass  # Placeholder for exam-taking logic

s1 = Student("Bob", 20) # 构造对象，会自动调用构造方法
s1.display_info()  # Output: Name: Bob, Age: 20
```

- 对象完整内存结构

类是抽象的，也称之为“对象的模板”。我们需要通过类这个模板， 创建类的实例对象，然后才能使用类定义的功能。

![PixPin\_2026\-07\-30\_09\-15\-15\.png](图片和附件/PixPin_2026-07-30_09-15-15.png)

## \_\_init\_\_构造方法和 \_\_new\_\_ 方法

\_\_init\_\_ 方法用于初始化对象。初始化是在对象创建后执行的一些操作，初始化当前对象的相关属性，没有返回值。

1. 方法名为 \_\_init\_\_ ，名称固定不可改。

2. 第一个参数固定，必须是 self，指的是刚创建好的实例对象。

3. 构造函数通常用来初始化实例对象的实例属性，如下代码就是初始化实例属性：name 和 age

```Python
def __init__(self, name, age):
    self.name = name
    self.age = age
```

4. 通过 `类名(参数列表)` 来调用构造函数。调用后，将创建好的对象返回给相应的变量，比如：`s1 = Person('张三', 19)`

5. \_\_init\_\_\(\) 方法：初始化创建好的对象，给实例属性赋值。\_\_new\_\_\(\) 方法: 用于创建对象，一般无需重定义该方法。

6. 如果不定义 \_\_init\_\_ 方法，系统会提供一个默认的 \_\_init\_\_ 方法，不做任何操作。如果定义了带参数的 \_\_init\_\_ 方法，系统不会默认创建这个方法。

> Python中的 self 相当于 C\+\+中的 this指针 ，JAVA和C\#中的 this 关键字。Python中， self 必须为构造函数的第一个参数，名字可以任意修改。但一般惯例，都叫做 self。
> 
> 

## 实例属性

实例属性是从属于实例对象的属性，也称为“实例变量”。它的使用有以下几个要点：

- 实例属性一般在 `__init__()` 方法中通过如下代码定义：`self.实例属性名 = 初始值`。但是也可以在实例方法中定义新的实例属性。

- 类的其他实例方法中，也是通过 `self `访问实例属性：`self.实例属性名`

- 创建实例对象后，通过实例对象访问：

    - `obj = 类名`   \# 创建和初始化对象，调用 \_\_init\_\_\(\) 初始化实例属性

    - `obj1.实例属性名 = 值`  \# 可以给已有的属性赋值，也可以新加属性

```Python
class Student:
    def __init__(self, name, score):
        '''
            1、在 __init__ 方法中定义实例属性 name 和 score
        '''
        self.name = name  # 增加 name 实例属性
        self.score = score  # 增加 score 实例属性

    def output_score(self):
        '''
            2、在 output_score 实例方法中定义实例属性 age
        '''
        self.age = 18  # 增加 age 实例属性
        print(f"Name: {self.name}, Score: {self.score}, Age: {self.age}")

stu = Student("Alice", 90)
print(stu.name, stu.score)

stu.output_score()  # 调用 output_score 方法
print(stu.age)  # 输出实例属性 age, 必须在调用 output_score 方法之后才能访问

'''
    3、在类的外部为实例 stu 添加一个新的实例属性 salary
'''
stu.salary = 200000
print(f"Salary: {stu.salary}")
```

## 实例方法

实例方法是从属于对象的方法。定义如下：

```Python
def func_name(self [, 形参列表]):
    函数体
```

方法的调用格式为：`对象.方法名([实参列表])`

> 要点：
> 
> - 定义实例方法时，`第一个参数必须是 slef`，self 指当前的实例对象。
> 
> - 调用实例方法时，`不需要也不能给 self 传参`。self 由解释器自动传参。
> 
> 

> 函数和方法的区别：
> 
> 1. 都是用来完成一个功能的语句块，本质一样。
> 
> 2. 方法调用时，通过对象来调用。方法从属于特定实例对象，普通函数没有这个特点。
> 
> 3. 直观上，方法定义时需要传递 self，函数不需要。
> 
> 

- 实例对象的方法调用本质

```Python
class Student:
    def say_name(self, name):
        print(f"My name is {name}")

stu = Student()

# 1、调用 say_name 方法
stu.say_name("Alice")

# 2、通过类名调用 say_name 方法，并传入实例 stu
Student.say_name(stu, "Bob")
```

![PixPin\_2026\-07\-30\_22\-53\-10\.png](图片和附件/PixPin_2026-07-30_22-53-10.png)

- 其它操作

```Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print('hello')

p = Person('Alice', 30)

'''
    1、dir(obj) -> 可以获取对象的所有属性、方法

    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
     '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__',
     '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
     '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
     '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
     '__static_attributes__', '__str__', '__subclasshook__', '__weakref__',
     'age', 'greet', 'name']
'''
print(dir(p))  # 输出实例 p 的所有属性和方法，返回列表对象

'''
    2、obj.__dict__ -> 可以获取对象的所有实例属性，返回字典对象，不包括实例方法
    
    {'name': 'Alice', 'age': 30}
'''
print(p.__dict__)  # 输出实例 p 的所有实例属性，返回字典对象

'''
    3、isinstance(obj, class) -> 判断对象是否是指定类的实例，返回布尔值
'''
print(isinstance(p, Person))  # 判断实例 p 是否是 Person 类的实例，返回布尔值
```

## 类对象

类本身也是一个对象。

当在使用 class 语句定义一个类时，就会创建一个类对象。

```Python
class Student:
    pass

print(Student) # <class '__main__.Student'>
print(type(Student)) # <class 'type'> 类对象的类型都是 type
print(id(Student)) # 1345009769008

Stu = Student # 将 Student 类赋值给 Stu 变量，Stu 现在是 Student 类的别名

# 实例
s = Stu()
print(s) # <__main__.Student object at 0x0000021A9B8C7D30>
print(type(s)) # <class '__main__.Student'> 实例对象的类型是类对象
print(id(s)) # 1345008350080
```

## 类属性

类属性从属于类对象，也称为“类变量”。由于类属性从属于类对象，可以**被所有实例对象共享**。

在**类中或者类的外面**，我们可以通过： **类名\.类变量名 来读写**。

类属性定义：

```Python
class 类名:
    类变量名 = 初始值
```

```Python
class Student:
    company = '北京大学' # 类属性 company
    obj_count = 0 # 类属性 obj_count

    def __init__(self, name, score):
        self.name = name  # 实例属性 name
        self.score = score  # 实例属性 score
        Student.obj_count += 1  # 每创建一个实例，obj_count 加 1

    def say_score(self):
        print(f"Name: {self.name}, Score: {self.score}, Company: {Student.company}")

s1 = Student("Alice", 90)
s1.say_score()  # 输出实例 s1 的信息

print(f'company: {Student.company}, obj_count: {Student.obj_count}')

'''
    为类 Student 添加一个新的类属性 other
'''
Student.other = '清华大学'
print(f'other: {Student.other}') # 输出类属性 other
```

![PixPin\_2026\-07\-30\_23\-19\-41\.png](图片和附件/PixPin_2026-07-30_23-19-41.png)

## 类方法\_静态方法

1. 类方法

类方法是从属于“类对象”的方法。类方法通过装饰器 `@classmethod` 来定义。

```Python
@classmethod 
def  类方法名(cls [，形参列表]):
    方法体
```

![PixPin\_2026\-07\-30\_23\-35\-56\.png](图片和附件/PixPin_2026-07-30_23-35-56.png)

2. 静态方法

Python中允许定义与“类对象”无关的方法，称为“静态方法”。 “静态方法”和在模块中定义普通函数没有区别，只不过“静态方法”放 到了“类的名字空间里面”，需要通过“类调用”。

![PixPin\_2026\-07\-30\_23\-40\-20\.png](图片和附件/PixPin_2026-07-30_23-40-20.png)

```Python
class Student:
    company = "SXT"     # 类属性

    @classmethod
    def printCompany(cls): # 类方法
        print(cls.company)

    @staticmethod
    def add(a, b):  # 静态方法
        print("{0}+{1}={2}".format(a, b, (a+b)))
        return a+b
```

## \_\_del\_\_\(\) 析构函数和垃圾回收机制

- \_\_del\_\_\(\) 称为“析构方法”，用于实现对象被销毁时所需的操作。比如： 释放对象占用的资源，例如：打开的文件资源、网络连接等。

- Python实现自动的垃圾回收，**当对象没有被引用时（引用计数为 0），由垃圾回收器调用 \_\_del\_\_\(\)**。

- 也可以通过 `del 语句`删除对象，也会调用 \_\_del\_\_\(\) 析构函数。

- 系统会自动提供 \_\_del\_\_ 方法，一般不需要自定义析构函数。

```Python
class Person:
    def __del__(self):
        print('对象被销毁了')

p = Person()
p2 = Person()
del p2
print("程序结束")

# 输出
# 对象被销毁了
# 程序结束
# 对象被销毁了
```

## \_\_call\_\_方法和可调用对象

![PixPin\_2026\-07\-31\_09\-00\-22\.png](图片和附件/PixPin_2026-07-31_09-00-22.png)

> - Python 中，凡是可以将 \(\) 直接应用到自身并执行，都称为可调用对象。 
> 
> - 可调用对象包括自定义的函数、Python 内置函数、以及本节所讲的实例对象。 
> 
> - 定义了 \_\_call\_\_\(\) 的对象，称为“可调用对象”，即该对象可以像函数一样被调用。 
> 
> - 该方法使得实例对象可以像调用普通函数那样，以“**对象名\(\)**”的形式使用（不是类名\(\)）。
> 
> 

```Python
def f1():
    print("f1")

f1()   # 本质也是调用了__call__() 方法

print(dir(f1)) # 输出函数 f1 的所有属性和方法，其中也是有 __call__() 方法的
```

```Python
class Car:
    def __call__(self, age,money):
        print("__call__方法")
        print("车龄：{0},金额：{1}".format(age,money))

f2 = Car()
f2(3,200000)    # 像调用函数那样调用，本质也是调用了 __call__()
```

