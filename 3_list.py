
 # List is a versatile data structure used to store an ordered collection of items in a single variable

server_list = ["one", 2, 3, 4, 5, "six", 7, 8, "nine", 10, True, False, 13.1] 
 #list may consists of any datatype

print (server_list) #it prints all the list in case you want to print the particular elements from the list then

element_1 = server_list [0]
print ("first element in the list: ", element_1)

 #in python indexing starts with "0"

'''
In list datatype there is an feature called slicing. which means instead of calling the overall list or individual to want to call the alternative elements.
format= [start index : last index : step size]  
-- default step_size is "1"
'''
 #print 1st 5 elements from server_list
print ("1st 5 elements are : ", server_list[0:5])
 #1st 5 elements are :  ['one', 2, 3, 4, 5]    # [1, 1+1, 2+1, 3+1, 4+1]

 #print alternative elements until 10th elements from server_list
print ("alternative elements until 10th elements are : ", server_list[0:10:2]) 

 #negative indexing

 #print last 5 elements from server_list
print ("last 5 elements from server_list are : ", server_list[-1:-6:-1]) 

 # if need to modify any element (mutable)
 # server_list[element index value] = new element value

server_list [2] = "three"

print ("mutated list : ", server_list)
print (server_list[2])


#print (dir(server_list))
'''
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort' -useful operations

'''

#append (only one element can be append at a time)

server_list.append(14)
print (server_list)

# for multi indexing
server_list.append([15.1,"sixteen"])
# ['one', 2, 'three', 4, 5, 'six', 7, 8, 'nine', 10, True, False, 13.1, 14, [15.1, 'sixteen']]

print(server_list)

# to print the last element 
print(server_list[-1][1])  # to print the last element

print(server_list[0:16:2])

#extend - is to add the list of elements to the existing list as an individual elements

server_list.extend([16,17.0,"eighteen", True])
print(server_list, "count of total elements is ", len(server_list))

# index - is to find the index of the element
print(server_list.index(True))

#in case similar value is available to find out we have to add the 1st index no. + 1 to the value
print(server_list.index(True, 10+1))

#insert = to add the element in to the particualr index value
server_list.insert(10, "eleven")

print(server_list)
#['one', 2, 'three', 4, 5, 'six', 7, 8, 'nine', 10, 'eleven', True, False, 13.1, 14, [15.1, 'sixteen'], 16, 17.0, 'eighteen', True]

# remove is to remove the element from the list.
server_list.remove(True)
print(server_list)

#case1: to remove the similar value present in further in list  by skipping 1st one. 
#server_list.remove(True, 10+1)

#reverse is to reverse the list from end to start
server_list.reverse()
print(server_list)
# (or)
server_list = server_list[:: -1]
print(server_list)


server_list = [3, 5,1, 2.0]
#server_list.sort()
print(server_list)

server_list1 = sorted(server_list)
print (server_list, server_list1)

#count is to find the element, how many times it repeated in the list.

server_list = ["one", 2, 3, True, 4, 5, "six", 7, True, 8, "nine", 10, True, False, 13.1] 

print(server_list.count(True))