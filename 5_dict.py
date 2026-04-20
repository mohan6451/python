# we can represent the dictionary datatype as 

server_list ={"one", 2, 3, 4, 5, "six", 7, 8, "nine", 10, True, False, 13.1}  # server_list = dict()

# dict are key value pairs and also called as hashmaps

env_list = {'prd' : "production", 'stg' : "preProduction", 'uat' : "user_acceptance_testing" , 'plt' : "performance_testing", 'try' : 'demo' }

print(env_list.get('prd'), env_list['plt'])

# dictionary is a mutable datatype

env_list['try'] = "sandbox"

print(env_list.get('try'))