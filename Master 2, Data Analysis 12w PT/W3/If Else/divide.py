num = 15  

if num % 3 == 0 or num % 5 == 0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")

# Explanation:
#     num = 15:
#         This line creates a variable called num and assigns it a value. You can change this value to test different numbers.
#     if num % 3 == 0 or num % 5 == 0::
#         The % operator is the modulus operator, which gives the remainder of the division.
#         num % 3 == 0 checks if num is divisible by 3 (remainder is 0).
#         num % 5 == 0 checks if num is divisible by 5.
#         The or operator checks if either of these conditions is true.
#     print("This number is divisible by 3 or 5"):
#         If either condition is true, this message is printed.
#     else::
#         If neither condition is true, the code inside the else block is executed.
#     print("This number is not divisible by 3 or 5"):
#         If num is not divisible by 3 or 5, this message is printed.

num = 21

if num % 3 == 0 and num % 7 == 0:
    print("fizzbuzz") 
elif num % 3 == 0:
    print("fizz")  
elif num % 7 == 0:
    print("buzz")
else:
    print(num)

#The `fizzbuzz` condition needs to come first because it checks if the number is divisible by both 3 and 7. If you don't check this 
# condition first, the code might incorrectly print `fizz` or `buzz` for a number like 21, which is divisible by both.
#By placing `fizzbuzz` first, you ensure that the program correctly identifies and handles numbers divisible by both 3 and 7 before checking 
# if they are divisible by just one of those numbers. This prevents any overlap or missed conditions in the logic.