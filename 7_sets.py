'''
set is an unordered collection of elements. it doesn't support indexing
set removes duplicates and stores unique values
'''

server_list = {'a', 'b', 'c', 'b'} # or ('a', 'b', 'c')

print (server_list)    # result; {'c', 'b', 'a'}

# print(dir(set)) - to find the functions used with set datatype

'''
['add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
'''

server_list.add(6)

print(server_list)

s1 = {'a', 'b', 'b', 'd'}

s2 = {'b', 'c', 'a', 'g'}

s1.difference(s2)

print(s1)