''' 
python stores string as tuple 
hence strings are immutable datatype
'''
sample = "abc" #pyhton stores it as ('a', 'b', 'c')


love = "i love travelling and cooking"

print (love)
'''
love[0] = "we"
print (love)    # 'str' object does not support item assignment
'''

print(dir(love))