# is an immutable datatype. elements can't be replaced or added. 
#it can be represented in

variable = (2, 8, 13, 4, 5, 3, 4)

print (type(variable))


env_list = tuple(["PRD", "STG", "UAT", "PLT", "TRY"]) # or env_list = ("PRD", "STG", "UAT", "PLT", "TRY")
print (type(env_list))

print (dir(tuple))  # 'count', 'index' only these can be done when compared to list data type

print(variable.count(2), variable.count(14))  # is the value is not in the tuple list then it represents as "0"

print(variable.index(13)) # is to find the index value of the element

# we can convert the tuple to list and vise-versa is called as "type casting" or "data type conversion"

server_list = tuple(["one", 2, 3, 4, 5, "six", 7, 8, "nine", 10, True, False, 13.1] )

print(type(server_list)) # <class 'tuple'>

server_list_1 = list(server_list)

print(type(server_list_1))




