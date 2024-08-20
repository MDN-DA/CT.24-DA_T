# music = "classical"
# print(music == "classical")
# answer = int(1234)

# music = "classical"
# print(bool(music))
# shopping_list = []
# print(bool(shopping_list))
# num = 0
# print(bool(num))
# my_name = "Dave"
# print(bool(my_name))

# print("What is your name?")
# user_name=input("    >    ")
# if user_name:
#     print("Welcome to your new account", user_name)
# else:
#     print("You must provide a name to sign up!")

# print("What coat is always wet when you put it on?")

shop_list = [
    "milk",
    "bread",
    "free-range eggs",
    "jam",
    "butter",
    "banana"
]
print(shop_list)
add_items=input("    >    ")
if add_items in shop_list:
     print(f"{add_items} is already added!")
else:
     shop_list.append(add_items)
print(shop_list)

print(shop_list)
add_items=input("    >    ")
if add_items not in shop_list:
     shop_list.append(add_items)
print(shop_list)