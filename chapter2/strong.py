# a = "hello world"
# b=a[0:6]
# print(b)

#字符串连接
# s = ["北京","西安","天津","重庆","南昌","江西景德镇"]
# sep = "-->"
# str= sep.join(s)
# # str
# print(f'字符串连接：{str}')
# s="PythonProgramming"
# # 1.打印第一个和最后一个字符
# print(s[0],s[-1])
# # 2.切片取出python
# print(s[0:6])
# # 3.切片取出gram
# print(s[9:13])
# # 5.将字符串逆序输出
# print(s[::-1])

text = " I love Python. Python is fun! "

# 1. 去除字符串两边空格
t1 = text.strip()
print(t1)   # "I love Python.      Python is fun!"

# 2. 统计单词 Python 出现次数
t2 = text.count("Python")
print(t2)   # 2

# 3. 转大写
t3 = text.upper()
print(t3)   # " I LOVE PYTHON.      PYTHON IS FUN! "

# 4. 替换操作
t4 = text.replace("Python.", "Python!")      # 句号 → 惊叹号
print(t4a)


