coffee_order = (
    "Alex - Cortado",
    "Ben - Latte",
    "Charlie - Mocha"
)

# print(coffee_order)
# coffee_order.append("Diane - Cappucino") 
# print(coffee_order)

# coffee_order = list(coffee_order)
# print(type(coffee_order))
# print(coffee_order)

answer=input("Who ordered a cortado? ")
while answer !="Alex":
    print("Incorrect")
    answer=input("Who ordered a cortado? ")
else:
    print("Enjoy your coffee!")