#python is case sensitive. ('A' not equal to 'a')

dict = "key value in the dictionary is mutable"

env = input("enter the environment to work with: ")
change_ticket = False

env = env.casefold()
if env == "prd":
    change_ticket = True
    print("please provide the change ticket")
elif env == 'stg':
    print("Welcome to staging environment")
else:
    print("please login with your credentials")