cost_per_exotic_mix_bag = 175
cost_per_apple_juice_1l = 85
#
glasses_per_bag = 3
glasses_per_1l = 4
#
num_glasses = int(input("How many glasses would you want to make? "))
#
cost_smoothie = (cost_per_exotic_mix_bag/glasses_per_bag) + (cost_per_apple_juice_1l/glasses_per_1l)
# 
total_cost = cost_smoothie * num_glasses
#
cost_per_exotic_mix_bag_in_pounds = cost_per_exotic_mix_bag/100
cost_per_apple_juice_1l_in_pounds = cost_per_apple_juice_1l/100
total_cost_in_pounds = total_cost/100
#
print(f"Total cost of Exotic Smoothie is: £{total_cost_in_pounds:.2f}")