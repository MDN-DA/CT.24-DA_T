# num1=int(input("Type your 1st number: "))
# num2=int(input("Type your 2nd number: "))

# print(num1*num2)

while True:
    try:
        num1=int(input("Type your 1st number: "))
        num2=int(input("Type your 2nd number: "))
        break
    except:
        print("That it not a whole number")
print(num1*num2)

# while True:
#     try:
#         num1=int(input("Type your 1st number: "))
#         num2=int(input("Type your 2nd number: "))
#     except:
#         print("That it not a whole number")