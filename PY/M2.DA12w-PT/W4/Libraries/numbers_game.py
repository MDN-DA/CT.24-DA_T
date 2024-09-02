import random

# print(random.random())
# print(random.uniform(1,10))
# print(random.randint(1000,9999)) #pin number

my_num = 88
com_num = random.randint(60,90)
while my_num != com_num:
    print(f"i picked {com_num} and you, the user, picked {my_num}!")
    com_num = random.randint(60,90)