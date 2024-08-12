cost_per_apple = 25
cost_per_banana = 50
#
num_apples = int(input("How many apples would you like to buy?"))
num_bananas = int(input("How many bananas would you like to buy?"))
#
cost_apples = num_apples * cost_per_apple
cost_bananas = num_bananas * cost_per_banana
total_cost = cost_apples + cost_bananas
#
cost_apples_in_pounds = cost_apples/100
cost_bananas_in_pounds = cost_bananas/100
total_cost_in_pounds = total_cost/100
#
print(f"Total cost of the apples is: £{cost_apples_in_pounds:.2f}")
print(f"Total cost of the bananas is: £{cost_bananas_in_pounds:.2f}")
print(f"Total cost of both combined is: £{total_cost_in_pounds:.2f}")