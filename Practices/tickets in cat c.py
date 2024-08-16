cost_per_adult_tickets_ubg = 4090
cost_per_junior_tickets_ubg = 2045
cost_per_adult_tickets_uw = 3850
cost_per_junior_tickets_uw = 1925
total_cost_ubg = cost_per_adult_tickets_ubg + (cost_per_junior_tickets_ubg*2)
total_cost_uw = cost_per_adult_tickets_uw + (cost_per_junior_tickets_uw*2)
total_cost_ubg_ga = cost_per_adult_tickets_ubg*3
total_cost_uw_ga = cost_per_adult_tickets_uw*3

cost_per_adult_tickets_max = 5740
cost_per_adult_tickets_min = 3030
cost_per_junior_tickets_max = 2870
cost_per_junior_tickets_min = 1700
total_cost_max = cost_per_adult_tickets_max + (cost_per_junior_tickets_max*2)
total_cost_min = cost_per_adult_tickets_min + (cost_per_junior_tickets_min*2)
total_cost_max_ga = cost_per_adult_tickets_max*3
total_cost_min_ga = cost_per_adult_tickets_min*3

cost_per_adult_tickets_ubg_v = cost_per_adult_tickets_ubg/100
cost_per_junior_tickets_ubg_v = cost_per_junior_tickets_ubg/100
cost_per_adult_tickets_uw_v = cost_per_adult_tickets_uw/100
cost_per_junior_tickets_uw_v = cost_per_junior_tickets_uw/100
total_cost_1 = total_cost_ubg/100
total_cost_2 = total_cost_uw/100
total_cost_3 = total_cost_ubg_ga/100
total_cost_4 = total_cost_uw_ga/100

cost_per_adult_tickets_max_v = cost_per_adult_tickets_max/100
cost_per_junior_tickets_min_v = cost_per_junior_tickets_max/100
cost_per_adult_tickets_max_v = cost_per_adult_tickets_min/100
cost_per_junior_tickets_min_v = cost_per_junior_tickets_min/100
total_cost_5 = total_cost_max/100
total_cost_6 = total_cost_min/100
total_cost_7 = total_cost_max_ga/100
total_cost_8 = total_cost_min_ga/100

print(f"Total cost, if it's Upper Behind Goal: £{total_cost_1}")
print(f"Total cost, if it's Upper Behind Goal (outside allocation): £{total_cost_3}")
print()
print(f"Total cost, if it's Upper Wing: £{total_cost_2}")
print(f"Total cost, if it's Upper Wing (outside allocation): £{total_cost_4}")
print()
print(f"Total cost, if it's Upper Center: £{total_cost_5} - it's maximum")
print(f"Total cost, if it's Upper Center (outside allocation): £{total_cost_7} - it's maximum")
print()
print(f"Total cost, if it's Upper Behind Goal Back: £{total_cost_6} - it's minimum")
print(f"Total cost, if it's Upper Behind Goal Back (outside allocation): £{total_cost_8} - it's minimum")