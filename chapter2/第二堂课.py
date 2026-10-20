# a = ['physics','chemistry',2017,2.5,[0.5,3]]
# # print(a_list[0],a_list[4],a_list[-1][0])
# # b=a[0:5]
# # b=a[:5]
# # b=a[0:]
# # b=a[:]
# # b=a[::3]
# # b=a[1:3]
# # b=a[-4:-2]
# b=a[1::3][1][0]
# print(a[1::3],b)


a = ['apple', 10, 4.5]
b = a+[12, 21]
b = a+[12, 21]
print(b)

#在末尾增加
b.append('XiaoLi')
#删
del b[-1]
#个数
print(len(b))

#数字
list = [1, 2, 4, 6, 4, 32, 54, 1, 1, 1, 66, 4, 66, 1]
print(f'最大：{max(list)}')
print(f'最小：{min(list)}')
#某元素在列表中出现次数
print(f'1在列表的出现次数：{list.count(1)}')

#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
n = [99, 100, 120, 150]
print(f'列表list内容：{list}')

list.extend(n)
print(f'在列表list末尾一次性追加n的多个值{list}')

print(f'从列表中找出1第一个匹配项的索引位置：{list.index(1)}')

print(f'移除列表中的一个元素（默认最后一个元素），并且返回该元素的值:{list.pop()}')

list.remove(1)
print(f'移除列表中某个值的第一个匹配项：{list}')

list.reverse()
print(f'反向列表中元素：{list}')

list1 = list.copy()
print(f'复制数组list,list1={list1}')


list.clear()
print('清空数组list', list)




