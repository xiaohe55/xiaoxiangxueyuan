# -*- coding:utf-8 -*-
'''
@author:coyote
@datetime:2019/1/25 22:24
@file: demo1_re.py
@function:正则表达式
'''
import re

# rs = re.match("chinahadoop", "chinahadoop.cn")
# print(rs)
# print(rs.group())

# .匹配非空字符
'''
rs = re.match(".", "a")
print(rs.group())
rs = re.match(".", "1")
print(rs.group())
rs = re.match("...", "abc")
print(rs.group())
rs = re.match(".", "\n")
print(rs)
'''

# \s匹配空白字符
'''
rs = re.match("\s", "\t")
print(rs)
rs = re.match("\s", "\n")
print(rs)
rs = re.match("\s", " ")
print(rs)
'''

# \S
'''
rs = re.match("\S", "\t")
print(rs)
rs = re.match("\S", "abc")
print(rs)
'''

# \w 单词字符
'''
rs = re.match("\w", "a")
print(rs)
rs = re.match("\w", "A")
print(rs)
rs = re.match("\w", "1")
print(rs)
rs = re.match("\w", "_")
print(rs)
rs = re.match("\w", "*")  # 非单词字符
print(rs)
rs = re.match("\w", "中过")
print(rs)
'''

# []
'''
rs = re.match("[Hh]", "hello")
print(rs)
rs = re.match("[Hh]", "Hello")
print(rs)

rs = re.match("[0123456789]", "334")
print(rs)
# 等价
rs = re.match("[0-9]", "334")
print(rs)
'''

# 数量表示方法
# *任意次
'''
rs = re.match("1\d*", "1234567")
print(rs.group())
rs = re.match("1\d*", "1234567abc")
print(rs.group())
'''

# +至少出现一次
'''
rs = re.match("\d+", "abc123")
print(rs)
rs = re.match("\d+", "1abc123")
print(rs)
rs = re.match("\d+", "12345abc123")
print(rs)
'''

# ?之多一次(0次或者1次）
'''
rs = re.match("\d?", "abc")
print(rs)
rs = re.match("\d?", "123abc")
print(rs)
'''

# {m} 固定次数
'''
rs = re.match("\d{3}", "12abc")
print(rs)
'''
# {m,}
'''
rs = re.match("\d{1,}", "1234567abc") #等价于+至少一次
print(rs)
'''
# {m,n}
'''
rs = re.match("\d{0,1}", "abc") #等价于?至多一次
print(rs)
'''
# 匹配11位手机号
'''
# 11位，第一位1，第二位3578， 第3位到11位是0-9任意数字
rs = re.match("1[3578]\d{9}", "13581587894")
print(rs)
rs = re.match("1[3578]\d{9}", "14581587894")  # 非法手机号
print(rs)
rs = re.match("1[3578]\d{9}", "13581587894abc")  # 非法手机号
print(rs)
'''

# 转义字符处理
# str1 = "hello\\world"
# print(str1)
# str2 = "hello\\\\world"
# print(str2)
# 原生字符串
'''
str3 = r"hello\\world"
print(str3)
rs = re.match("\w{5}\\\\\\\\\w{5}", str3)
print(rs)
rs = re.match(r"\w{5}\\\\\w{5}", str3)
print(rs)
'''

# 边界表示
# $字符串结尾
'''
rs = re.match("1[3578]\d{9}$", "13581587894")
print(rs.group())
rs = re.match("1[3578]\d{9}$", "13581587894abc")
print(rs)
'''
# 邮箱匹配
'''
rs = re.match("\w{3,10}@163\.com$", "hello_124@163.com")
print(rs)
# rs = re.match("\w{3,10}@163.com$", "he@163.com")
# print(rs)
rs = re.match("\w{3,10}@163\.com$", "hello_124@163mcom")
print(rs)
'''
# \b \B 单词边界
# rs = re.match(r".*\bpython\b", "hi python hello")
# print(rs)
#  \B 非单词边界
# rs = re.match(r".*\Bth\B", "hi python hello")
# print(rs)

# 匹配分组
# 匹配0到100之间的数字
'''
1)0-9单独的 数字，不能使01,02等格式
2）十位：1-9，个位：0-9
3)最大数字是100
'''
# rs = re.match(r"[1-9]\d?$|0$|100$", "100")
# print(rs)
# rs = re.match(r"[1-9]\d?$|0$|100$", "0")
# print(rs)
# rs = re.match(r"[1-9]\d?$|0$|100$", "12")
# print(rs)
# rs = re.match(r"[1-9]\d?$|0$|100$", "02")
# print(rs)
# rs = re.match(r"[1-9]\d?$|0$|100$", "200")
# print(rs)
# rs = re.match(r"[1-9]?\d?$|100$", "0")
# print(rs)

# ()分组
'''
rs = re.match("\w{3,10}@(163|qq|outlook)\.com$", "hello@163.com")
print(rs)
rs = re.match("\w{3,10}@(163|qq|outlook)\.com$", "123456@qq.com")
print(rs)
rs = re.match("\w{3,10}@(163|qq|outlook)\.com$", "hello@outlook.com")
print(rs)
'''

# \num
# html_str = "<head><title>python</title></head>"
# rs = re.match(r"<.+><.+>.+</.+></.+>", html_str)
# print(rs)

# html_str2 = "<head><title>python</head></title>"
# rs = re.match(r"<.+><.+>.+</.+></.+>", html_str2)
# print(rs)

'''
html_str = "<head><title>python</title></head>"
html_str2 = "<head><title>python</head></title>"
rs = re.match(r"<(.+)><(.+)>.+</\2></\1>", html_str)
print(rs)
rs = re.match(r"<(.+)><(.+)>.+</\2></\1>", html_str2)
print(rs)
'''

# 别名
'''
html_str = "<head><title>python</title></head>"
rs = re.match(r"<(?P<g1>.+)><(?P<g2>.+)>.+</(?P=g2)></(?P=g1)>", html_str)
print(rs)
'''

# search 自一次出现
# rs = re.search("car", "haha car carbal abcar carbal")
# print(rs)

# findall
# rs = re.findall("car", "haha car carbal abcar carbal")
# print(rs)
# mail_str ="zhangsan:helloworld@163.com,lisi:123456@qq.cn"
# rs=re.findall(r"(\w{3,20}@(163|qq)\.(com|cn))", mail_str)
# print(rs)

# finditer
'''
mail_str ="zhangsan:helloworld@163.com,lisi:123456@qq.cn"
itor = re.finditer(r"\w{3,20}@(163|qq)\.(com|cn)", mail_str)
for it in itor:
    print(it.group())
'''

# sub
# str = "java python c c++ java"
# rs = re.sub(r"java", "python", str)
# print(rs)
'''
str_test = "apple=5,banana=3,orange=2"


def update_price(result):
    price = result.group()
    new_price = int(price) +1

    print(price)
    return str(new_price)


rs = re.sub(r"\d+", update_price, str_test)
print(rs)

# split
price_list = str_test.split(",")
for price in price_list:
    print(price)

'''


# 贪婪模式
'''
rs = re.findall(r"hello\d*", "hello12345")
print(rs)
rs = re.findall(r"hello\d+", "hello12345")
print(rs)
rs = re.findall(r"hello\d?", "hello12345")
print(rs)
rs = re.findall(r"hello\d{2,}", "hello12345")
print(rs)
rs = re.findall(r"hello\d{1,3}", "hello12345")
print(rs)
'''


# 非贪婪模式
rs = re.findall(r"hello\d*?", "hello12345")
print(rs)
rs = re.findall(r"hello\d+?", "hello12345")
print(rs)
rs = re.findall(r"hello\d??", "hello12345")
print(rs)
rs = re.findall(r"hello\d{2,}?", "hello12345")
print(rs)
rs = re.findall(r"hello\d{1,3}?", "hello12345")
print(rs)
