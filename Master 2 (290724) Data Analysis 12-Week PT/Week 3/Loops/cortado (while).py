answer = input("Who ordered a cortado? ")

while answer != "Alex":
    print("incorrect")
    answer = input("That's wrong, Try again? ")
else:
    print("correct")