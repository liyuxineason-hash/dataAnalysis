# -*- coding: utf-8 -*-
"""
Python数据分析课件 第1、2、3章 Python方法与函数总结
来源：《Python数据分析与科学计算》第1章 数据分析基础、第2章 Python数据分析环境、第3章 Python数据类型
"""

# ============================================================
# 第1章 数据分析基础 & 第2章 Python数据分析环境
# ============================================================
# 这两章主要为概念介绍和环境搭建，涉及的Python基础函数如下：

# 1. print() 函数
# 功能：输出信息到控制台
print('Hello World!')                    # 输出字符串
print('a =', 10, 'b =', 20)             # 输出多个值，用逗号分隔
print('Hello', end=' ')                  # end参数控制行尾
print('World')

# 2. input() 函数
# 功能：从键盘读取用户输入，返回字符串类型
# name = input('请输入你的名字:')
# print('你好,', name)

# 3. type() 函数
# 功能：返回对象的类型
print(type(123))          # <class 'int'>
print(type(3.14))         # <class 'float'>
print(type('hello'))      # <class 'str'>
print(type(True))         # <class 'bool'>
print(type([1, 2]))       # <class 'list'>
print(type((1, 2)))       # <class 'tuple'>
print(type({1: 'a'}))     # <class 'dict'>
print(type({1, 2}))       # <class 'set'>

# 4. id() 函数
# 功能：返回对象的内存地址
x = 10
print(id(x))              # 输出变量x的内存地址

# 5. str() 函数
# 功能：将其他类型转换为字符串
s = str(123)
print(s, type(s))         # 123 <class 'str'>

# 6. ord() 函数
# 功能：返回字符对应的ASCII码（Unicode码点）
print(ord('A'))           # 65
print(ord('a'))           # 97
print(ord('0'))           # 48

# 7. chr() 函数
# 功能：将ASCII码（Unicode码点）转换为对应字符（ord的逆运算）
print(chr(65))            # 'A'
print(chr(97))            # 'a'

# 8. bytes 类型（第2章提到Python3.x新增）
b = b'Python'
print(b, type(b))         # b'Python' <class 'bytes'>


# ============================================================
# 第3章 Python数据类型
# ============================================================

# ============================================================
# 3.1 基本数据类型
# ============================================================
# 整型 int
a = 12345678900123456789
b = a * a
print(b)

# 不同进制整数
print(0b1010)             # 二进制：10
print(0o17)               # 八进制：15
print(0xFF)               # 十六进制：255

# 浮点型 float
print(3.14)               # 十进制小数形式
print(1.2e-3)             # 指数形式（科学计数法）

# 字符串 str
print("Let's go")        # 双引号内可包含单引号
s = "'Python' Program"
print(s)

# 布尔型 bool
print(type(True))          # <class 'bool'>
print(True == 1)           # True
print(False == 0)          # True

# 复数 complex
x = 3 + 5j
print(x.real)              # 3.0 实部
print(x.imag)              # 5.0 虚部
y = 6 - 10j
print(x + y)               # (9-5j)

# ============================================================
# 3.2 运算符与表达式
# ============================================================
# 算术运算符
print(3 / 5)               # 0.6  除法
print(3 // 5)              # 0    整除
print(-3.0 // 5)           # -1.0 整除（向下取整）
print(2 ** 3)              # 8    乘方
print(4 * 3 ** 2)          # 36   优先级
print(10 % 3)              # 1    取余
print('a' * 10)            # 字符串重复

# 赋值运算符
x = y = 5                  # 链式赋值
x, y, z = 2, 5, 8          # 多变量并行赋值
x, y = y, x                # 交换两个变量的值

# 复合赋值运算符
a = 3
b = 5
a += b                     # 等价于 a = a + b
print(a)                   # 8
a %= 3                     # 等价于 a = a % 3
print(a)                   # 2
a >>= 1                    # 等价于 a = a >> 1
print(a)                   # 1

# 关系运算符
print(3 > 5)               # False
print(3 == 3)              # True

# 逻辑运算符
print(True and 0)          # 0  (and短路)
print(False and 12)        # False
print(True or 0)           # True
print(False or 12)         # 12
print(not True)            # False

# 成员运算符
print('a' in 'abcd')       # True
print('ac' in 'abcd')      # False
print('a' not in 'bcd')    # True
print(3 not in [1, 2, 3, 4])  # False

# 同一性运算符
x = y = 2.5
z = 2.5
print(x is y)              # True
print(x is z)              # False（不同对象）
print(x is not z)          # True

# 位运算符
print(5 & 3)               # 1  按位与
print(5 | 3)               # 7  按位或
print(5 ^ 3)               # 6  按位异或
print(~5)                  # -6 按位取反
print(57 << 4)             # 912 左移
print(57 >> 4)             # 3   右移

# ============================================================
# 3.3.1 列表（list）
# ============================================================
# 列表创建
a_list = ['physics', 'chemistry', 2017, 2.5]
b_list = ['wade', 3.0, 81, ['bosh', 'haslem']]
c_list = []
print(a_list)

# 列表元素读取（索引）
print(a_list[1])           # 'chemistry'
print(a_list[-1])          # 2.5

# 列表切片
print(a_list[1:3])         # ['chemistry', 2017]
print(a_list[1:-1])        # ['chemistry', 2017]
print(a_list[:3])          # ['physics', 'chemistry', 2017]
print(a_list[1:])          # ['chemistry', 2017, 2.5]
print(a_list[:])           # 完整列表
print(a_list[::2])         # 步长为2

# --- 列表方法 ---

# append()：向列表尾部添加一个元素
a_list.append('Python')
print(a_list)

# extend()：将一个列表中的所有元素添加到原列表尾部
a_list.extend([2017, 'C'])
print(a_list)

# insert()：将元素插入到列表的指定位置
a_list.insert(3, 3.5)
print(a_list)

# index()：获取指定元素首次出现的下标
# 格式：index(value[, start[, end]])
a_list = ['physics', 2017, 'chemistry', 3.5, 2.5, [0.5, 3], 5, 'Python', 2017, 'C']
print(a_list.index(2017))          # 1
print(a_list.index(2017, 2))       # 8

# count()：统计列表中指定元素出现的次数
print(a_list.count(2017))          # 2
print(a_list.count([0.5, 3]))      # 1

# remove()：删除首次出现的指定元素
a_list.remove(2017)
print(a_list)

# pop()：删除并返回指定位置的元素（默认最后一个）
a_list2 = [10, 7, 1.5]
print(a_list2.pop())       # 1.5
print(a_list2)             # [10, 7]

# reverse()：将列表中的元素翻转存放（原地修改）
a_list2.reverse()
print(a_list2)             # [7, 10]

# sort()：对列表进行排序（原地修改，覆盖原列表）
a_list2.sort()             # 默认升序
print(a_list2)             # [7, 10]
a_list2.sort(reverse=True) # 降序
print(a_list2)             # [10, 7]

# del 命令：删除列表中指定位置的元素或删除整个列表
c_list2 = [10, 7, 1.5]
del c_list2[1]
print(c_list2)             # [10, 1.5]

# --- 列表常用内置函数 ---

# len()：返回列表的元素个数
print(len(a_list))
print(len([1, 2.0, 'hello']))  # 3

# max()：返回列表中的最大值
d_list = ['123', 'xyz', 'zara', 'abc']
print(max(d_list))         # 'zara'

# min()：返回列表中的最小值
print(min(d_list))         # '123'

# sum()：对数值列表求和
print(sum([23, 59, -1, 2.5, 39]))  # 122.5

# sorted()：对列表排序，返回新列表，不改变原列表
a_list3 = [80, 48, 35, 95, 98, 65, 99, 95, 18, 71]
print(sorted(a_list3))                    # 升序
print(sorted(a_list3, reverse=True))      # 降序
print(a_list3)                            # 原列表不变

# id()：获取对象的内存地址
print(id(a_list3))

# 列表应用举例：逆置输入数据
b_input = '1,2,3,4,5'
r_list = []
for i in b_input.split(','):
    r_list.append(i)
print('逆置前:', r_list)
n = len(r_list)
for i in range(n // 2):
    r_list[i], r_list[n - i - 1] = r_list[n - i - 1], r_list[i]
print('逆置后:', r_list)

# ============================================================
# 3.3.2 元组（tuple）
# ============================================================
# 元组创建
a_tuple = ('physics', 'chemistry', 2017, 2.5)
b_tuple = (1, 2, (3.0, 'hello world!'))
d_tuple = ()
x = (1)        # 这是整数1，不是元组
y = (1,)       # 只有一个元素时需要加逗号
print(x, y)    # 1 (1,)

# 元组元素读取
print(a_tuple[1])          # 'chemistry'
print(a_tuple[-1])         # 2.5

# 元组切片
print(a_tuple[1:3])        # ('chemistry', 2017)
print(a_tuple[::3])        # ('physics', 2.5)

# index()：获取指定元素首次出现的下标
print(a_tuple.index(2017)) # 2

# count()：统计元组中指定元素出现的次数
print(a_tuple.count(2017)) # 1
print(a_tuple.count(1))    # 0

# in 成员运算
print('chemistry' in a_tuple)  # True

# del 命令：删除元组
# del a_tuple

# tuple()：将列表转换为元组
a_list4 = ['physics', 'chemistry', 2017, 2.5]
print(tuple(a_list4))

# list()：将元组转换为列表
b_tuple2 = (1, 2, (3.0, 'hello world!'))
print(list(b_tuple2))

# type()：返回对象类型
print(type(a_list4))       # <class 'list'>
print(type(b_tuple2))      # <class 'tuple'>

# 元组解包赋值
v = ('Python', 2, True)
(x1, y1, z1) = v
print(x1, y1, z1)          # Python 2 True

# ============================================================
# 3.3.3 字符串（str）
# ============================================================
# 字符串创建
str1 = 'Hello'
str2 = "Program \n'Python'"
print(str1)
print(str2)

# 三重引号字符串
str3 = 'Python is an "object-oriented"\nopen-source programming language'
print(str3)

# 字符串元素读取
print(str1[0])             # 'H'
print(str1[-1])            # 'o'

# 字符串分片（切片）
s = 'Python Program'
print(s[0:5:2])            # 'Pto'
print(s[:])                # 'Python Program'
print(s[-1:-20:-1])        # 'margorP nohtyP'

# 字符串连接（+运算符）
print('Hello' + 'World')   # 'HelloWorld'

# 字符串重复（*运算符）
print('Hello' * 3)         # 'HelloHelloHello'

# 字符串关系运算（按ASCII码比较）
print('a' == 'a')          # True
print('a' == 'A')          # False
print('abc' < 'abd')       # True

# 成员运算
print('ab' in 'aabb')      # True
print('abc' in 'aabbcc')   # False
print('a' not in 'abc')    # False

# --- 字符串常用方法 ---

# find()：查找子串首次出现的位置，找不到返回-1
# 格式：str.find(substr[, start[, end]])
s1 = "beijing xi'an tianjin beijing chongqing"
print(s1.find('beijing'))          # 0
print(s1.find('beijing', 3))       # 22
print(s1.find('beijing', 3, 20))   # -1

# replace()：字符串替换
# 格式：str.replace(old, new[, max])
s2 = 'this is string example. this is string example.'
print(s2.replace('is', 'was'))          # 全部替换
print(s2.replace('is', 'was', 2))       # 最多替换2次

# split()：字符串分离，返回列表
# 格式：str.split([sep])
s3 = "beijing,xi'an,tianjin,beijing,chongqing"
print(s3.split(','))       # 按逗号分离
print(s3.split('a'))       # 按字母a分离
print(s3.split())          # 按空白字符分离

# join()：字符串连接，将序列中的元素以指定字符连接
# 格式：sep.join(sequence)
s4 = ['beijing', "xi'an", 'tianjin', 'chongqing']
sep = '-->'
result = sep.join(s4)
print(result)
s5 = ('Hello', 'World')
print(''.join(s5))         # 'HelloWorld'

# str()：将数值转换为字符串
print('Python' + str(3))   # 'Python3'

# ord()：将字符转换为ASCII码
print(ord('A'))            # 65

# chr()：将ASCII码转换为字符
print(chr(97))             # 'a'

# ============================================================
# 3.3.4 字典（dict）
# ============================================================
# 字典创建（使用=赋值）
a_dict = {'Alice': 95, 'Beth': 82, 'Tom': 65.5, 'Emily': 95}
print(a_dict)

# 空字典
b_dict = {}
print(b_dict)

# dict()函数创建字典
c_dict = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print(c_dict)
d_dict = dict(one=1, two=2, three=3)
print(d_dict)
e_dict = dict([('one', 1), ('two', 2), ('three', 3)])
print(e_dict)
f_dict = dict((('one', 1), ('two', 2), ('three', 3)))
print(f_dict)
g_dict = dict()
print(g_dict)

# fromkeys()：创建字典，用序列中的元素作为键，value为所有键的初始值
# 格式：dict.fromkeys(seq[, value])
h_dict = {}.fromkeys((1, 2, 3), 'student')
print(h_dict)
i_dict = {}.fromkeys((1, 2, 3))
print(i_dict)

# 字典元素读取（下标方法）
a_dict = {'Alice': 95, 'Beth': 82, 'Tom': 65.5, 'Emily': 95}
print(a_dict['Tom'])       # 65.5

# get()：获取指定键对应的值，键不存在时返回默认值
# 格式：dict.get(key, default=None)
print(a_dict.get('Alice'))          # 95
print(a_dict.get('a', 'address'))   # 'address'
print(a_dict.get('a'))              # None

# 字典元素添加与修改
a_dict['Beth'] = 79        # 修改已有键的值
a_dict['Eric'] = 98        # 添加新键值对
print(a_dict)

# update()：用另一个字典更新当前字典
a_dict2 = {'Alice': 95, 'Beth': 79, 'Emily': 95, 'Tom': 65.5}
b_dict2 = {'Eric': 98, 'Tom': 82}
a_dict2.update(b_dict2)
print(a_dict2)

# del命令：删除字典中指定键的元素
del a_dict2['Beth']
print(a_dict2)

# pop()：删除并返回指定键的元素
val = a_dict2.pop('Alice')
print(val)                 # 95

# popitem()：删除并返回字典中的一个键值对
item = a_dict2.popitem()
print(item)

# clear()：清空字典所有元素
a_dict3 = {'a': 1, 'b': 2}
a_dict3.clear()
print(a_dict3)

# --- 字典遍历方法 ---

# keys()：返回字典所有键
a_dict4 = {'Alice': 95, 'Beth': 82, 'Tom': 65.5, 'Emily': 95}
print(a_dict4.keys())

# values()：返回字典所有值
print(a_dict4.values())

# items()：返回字典所有键值对
print(a_dict4.items())

# 遍历字典
for k in a_dict4.keys():
    print(k, end=' ')
print()
for v in a_dict4.values():
    print(v, end=' ')
print()
for k, v in a_dict4.items():
    print(k, v, end='; ')
print()

# ============================================================
# 3.3.5 集合（set）
# ============================================================
# 集合创建（使用大括号）
a_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a_set)

# 集合自动去重
b_set = {1, 3, 3, 5}
print(b_set)               # {1, 3, 5}

# set()函数创建集合
b_set2 = set(['physics', 'chemistry', 2017, 2.5])
print(b_set2)
c_set = set(('Python', 'C', 'HTML', 'Java', 'Perl'))
print(c_set)
d_set = set('Python')
print(d_set)

# frozenset()：创建冻结集合（不可变集合，可作字典键）
e_set = frozenset('a')
a_dict5 = {e_set: 1, 'b': 2}
print(a_dict5)

# 集合访问（使用in或循环遍历）
b_set3 = set(['physics', 'chemistry', 2017, 2.5])
print(2.5 in b_set3)       # True
print(3 in b_set3)         # False
for i in b_set3:
    print(i, end=' ')
print()

# --- 集合方法 ---

# add()：向集合中添加一个元素
b_set3.add('math')
print(b_set3)

# update()：将多个集合/列表中的元素添加到集合中
s = {'Python', 'C', 'C++'}
s.update({1, 2, 3}, {'Wade', 'Nash'}, {0, 1, 2})
print(s)

# remove()：删除集合中指定元素（元素不存在时报错）
s2 = {0, 1, 2, 3, 'Python', 'Wade', 'C++', 'Nash', 'C'}
s2.remove(0)
print(s2)

# discard()：删除集合中指定元素（元素不存在时不报错）
s2.discard('C')
print(s2)
s2.discard('abc')          # 不存在，不报错
print(s2)

# pop()：删除并返回集合中任意一个元素
val = s2.pop()
print(val)

# clear()：清空集合所有元素
s3 = {1, 2, 3}
s3.clear()
print(s3)

# --- 集合运算 ---

# 交集（&）
print({0, 1, 2, 3, 4, 5, 7, 8, 9} & {0, 2, 4, 6, 8})

# 并集（|）
print({0, 1, 2, 3, 4, 5, 7, 8, 9} | {0, 2, 4, 6, 8})

# 差集（-）
print({0, 1, 2, 3, 4, 5, 6, 7, 8, 9} - {0, 2, 4, 6, 8})

# 对称差集（^）
print({0, 1, 2, 3, 4, 5, 6, 7, 8, 9} ^ {0, 2, 4, 6, 8})

# 集合比较
print({1, 2} == {1, 2})    # True
print({1, 2} != {1, 2})    # False
print({1, 2} < {1, 2, 3})  # True

# ============================================================
# 3.3 类型转换函数汇总
# ============================================================
# int()：转换为整型
print(int(3.14))           # 3
print(int('100'))          # 100

# float()：转换为浮点型
print(float(3))            # 3.0
print(float('3.14'))       # 3.14

# str()：转换为字符串
print(str(123))            # '123'

# list()：转换为列表
print(list((1, 2, 3)))     # [1, 2, 3]
print(list('abc'))         # ['a', 'b', 'c']

# tuple()：转换为元组
print(tuple([1, 2, 3]))    # (1, 2, 3)

# set()：转换为集合
print(set([1, 2, 2, 3]))   # {1, 2, 3}

# dict()：转换为/创建字典
print(dict([('a', 1), ('b', 2)]))

# frozenset()：转换为冻结集合
print(frozenset([1, 2, 3]))

# bool()：转换为布尔型
print(bool(0))             # False
print(bool(''))            # False
print(bool(None))          # False
print(bool(1))             # True
print(bool('hello'))       # True

# zip()：将多个序列打包为元组列表
print(list(zip(['a', 'b', 'c'], [1, 2, 3])))

# range()：生成整数序列（常用于for循环）
for i in range(5):
    print(i, end=' ')
print()
for i in range(2, 10, 2):
    print(i, end=' ')
print()

# sorted()：排序（适用于所有可迭代对象）
print(sorted('hello'))

# len()：返回对象长度
print(len('hello'))
print(len([1, 2, 3]))
print(len({'a': 1}))


# ============================================================
# 3.3.3 补充：字符串常用方法（续）
# ============================================================
text = " I love Python.      Python is fun! "

# strip()：去除字符串两边的空白字符（空格、\t、\n），中间的空格不动
t1 = text.strip()
print(t1)                  # "I love Python.      Python is fun!"
# 相关方法：
print("  hello  ".lstrip())    # 'hello  '  只去除左边空白
print("  hello  ".rstrip())    # '  hello'  只去除右边空白
print("**hello**".strip("*"))  # 'hello'    去除两边指定字符

# count()：统计子串在字符串中出现的次数（大小写敏感）
t2 = text.count("Python")
print(t2)                  # 2
print(text.count("python"))# 0（大小写敏感）

# upper()：全部转为大写
t3 = text.upper()
print(t3)                  # " I LOVE PYTHON.      PYTHON IS FUN! "

# lower()：全部转为小写
print("Hello World".lower())  # 'hello world'

# title()：每个单词首字母大写，其余小写
print("hello world".title())  # 'Hello World'

# capitalize()：仅首字母大写，其余全部小写
print("hello WORLD".capitalize())  # 'Hello world'

# swapcase()：大小写互换
print("Hello World".swapcase())    # 'hELLO wORLD'

# replace()：替换字符串中的子串
# 格式：str.replace(old, new[, max])
t4a = text.replace("Python.", "Python!")
print(t4a)                 # " I love Python!      Python is fun! "
print(text.replace(".", "!"))  # 所有句号替换为感叹号
print("I love Python, Python is fun".replace(",", "!"))  # 逗号替换为感叹号

# --- 重要特性：字符串不可变 ---
# 以上所有字符串方法都不会修改原字符串，而是返回一个新字符串
text = " I love Python.      Python is fun! "
text.strip()
print(text)                # 原样不变！
# 必须用变量接住结果：
text = text.strip()        # 重新赋值才真正"修改"了 text
print(text)

# --- 链式调用 ---
# 字符串方法返回新字符串，因此可以链式调用
result = text.strip().upper().replace(".", "!")
print(result)              # "I LOVE PYTHON!      PYTHON IS FUN!"


# ============================================================
# 补充：源代码（第3章 源代码 3.1~3.9.py）中的方法与函数
# ============================================================

# --- 格式化输出 ---

# % 格式化（旧式格式化，源代码 3.2.py、3.5.py、3.7.py、3.8.py 中使用）
a = 1
b = 2
c = '\101'                 # 八进制转义字符，'\101' = 'A'
print("\t%d\n%d%s\n%d%d\t%s" % (a, b, c, a, b, c))
# %d：格式化为整数
# %s：格式化为字符串
# %f：格式化为浮点数
# \t：制表符  \n：换行符
print("%d  its factors are：" % 6, [1, 2, 3])   # 3.5.py中输出完数及因子
print("共有%d个单词" % 5)                        # 3.7.py中输出统计结果
print('英文字母个数：%s' % 3)                     # 3.8.py中输出统计结果

# format() 方法（源代码 3.9.py 中使用）
# 用 {} 作为占位符进行格式化
print("重复元素有{}行，不重复元素有{}行".format(2, 3))
# 也可以指定位置：{0}、{1}
print("{0} 和 {1}".format("Python", "数据分析"))
# 也可以指定关键字参数
print("{name}的年龄是{age}".format(name="Tom", age=20))

# --- 源代码中出现的其他方法/函数 ---

# int()：将字符串或数字转换为整型（源代码 3.9.py）
x = int(input("请输入字符串行数n："))
# x = int("5")  # → 5

# list()：将可迭代对象转换为列表（源代码 3.8.py、3.9.py）
a_list = list(input('请输入一行字符：'))  # 将输入字符串的每个字符转为列表元素
print(list("abc"))         # ['a', 'b', 'c']

# set()：将可迭代对象转换为集合，自动去重（源代码 3.9.py）
list1 = [1, 2, 2, 3, 3, 3]
list2 = list(set(list1))
print(list2)               # [1, 2, 3]（去重后）

# ord()：返回字符的ASCII码（源代码 3.8.py 中判断字符类型）
print(ord('A'))            # 65
print(ord('a'))            # 97
print(ord('0'))            # 48

# range()：生成整数序列（源代码 3.4.py、3.5.py、3.6.py、3.7.py、3.8.py、3.9.py 中大量使用）
for i in range(5):          # 0 1 2 3 4
    print(i, end=' ')
print()
for i in range(1, 10):      # 1~9
    print(i, end=' ')
print()
for i in range(0, 10, 2):   # 0 2 4 6 8
    print(i, end=' ')
print()

# append()：向列表尾部添加元素（源代码 3.4.py、3.5.py、3.6.py、3.8.py、3.9.py）
L1 = []
L1.append(1)
L1.append(2)
print(L1)                  # [1, 2]

# split()：字符串分离（源代码 3.4.py）
b_list = "1,2,3,4,5"
a_list = b_list.split(',')
print(a_list)              # ['1', '2', '3', '4', '5']

# len()：返回对象长度（源代码 3.4.py、3.8.py、3.9.py）
print(len([1, 2, 3]))      # 3
print(len("hello"))        # 5

# input()：从键盘读取用户输入（源代码 3.4.py、3.6.py、3.7.py、3.8.py、3.9.py）
# word = input("请输入一个英文单词：")

# print()：输出到控制台（所有源代码文件中均使用）
print("Hello World!")
