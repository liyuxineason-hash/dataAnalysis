# a_list=[80, 48, 35, 95, 98, 65, 99, 95, 18, 71]
# print(sum(a_list))
# b_list=['123', 'xyz', 'zara', 'abc']
# # print(sum(b_list))
#


# a_list=[80, 48, 35, 95, 98, 65, 99, 95, 18, 71]
# print(sorted(a_list)) #默认升序
# print(sorted(a_list,reverse=True)) #降序

#不同类型的不能使用max或者min
# a = ['1','xyz','zara','abc']
# print(min(a))

# a = (1,2,3,4,5 )
# b=[1,2,3,4,5,6]
# print(f'元组：{a}')
# print(f'列表：{b}')

# a_tuple= ('physics', 'chemistry',2017, 2.5)
# print(a_tuple)
# print(f'切片，从索引1到索引3，不包括3，左闭右开：{a_tuple[1:3]}')
#
# print(f'从索引1到4（不包含），步长2，从索引1开始数两个：{a_tuple[1:4:2]}')



#集合 无序，不重复。
a = set(['hp','ch',2017,2.5,2017])
print(a)

#冻结集合
a = frozenset(a)
print(a)




