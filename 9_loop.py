

#while loop:

value = 1

# while value < 10:
#     print(value)
#     value = 1+ value

# while value < 10:
#     if value == 5:
#         break
#     print(value)
#     value = 1+ value

# while value < 10:
#     if value == 5:
#         continue
#     print(value)
#     value = 1+ value              it will stuck in loop have to be care while using continue      

while value < 10:
    if value == 5:
        print ("five")
        value = value + 1
        continue
    print(value)
    value += 1  # or     value = value +1 