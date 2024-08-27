cost_per_exotic_mix_bag = 185 # price in penny
cost_per_mango_bag = 199 # price in penny
cost_per_pineapple_bag = 199 # price in penny
cost_per_apple_juice_1l = 85

glasses_per_bag = 3
glasses_per_1l = 4

num_glasses = int(input("How many glasses would you want to make? "))

cost_exotic = (cost_per_exotic_mix_bag/glasses_per_bag) + (cost_per_apple_juice_1l/glasses_per_1l) # 166 gr = 3 glasses
cost_pm =  ((cost_per_pineapple_bag+cost_per_mango_bag)/(glasses_per_bag*2)) + (cost_per_apple_juice_1l/glasses_per_1l) # 75+83 = 158 gr = 6 glasses

total_cost1 = cost_exotic * num_glasses
total_cost2 = cost_pm * num_glasses


cost_per_exotic_mix_bag_in_pounds = cost_per_exotic_mix_bag/100 # switch to pounds
cost_per_mango_bag_in_pounds = cost_per_pineapple_bag/100 # switch to pounds
cost_per_pineapple_bag_in_pounds = cost_per_mango_bag/100 # switch to pounds
cost_per_apple_juice_1l_in_pounds = cost_per_apple_juice_1l/100
total_cost1_in_pounds = total_cost1/100
total_cost2_in_pounds = total_cost2/100

print(f"Total cost of Exotic Smoothie (Pineapple, Mango, Papaya) is: £{total_cost1_in_pounds:.2f}")
print(f"Total cost of Pineapple/Mango Smoothie is: £{total_cost2_in_pounds:.2f}")