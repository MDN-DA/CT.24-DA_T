username = input("Enter your Username: ")

for attempt in range(5):  # Allows up to 5 attempts
    password = input("Enter your Password: ")  
    if password == "TiramisuinPizeria":
        print("Correct! Welcome!")
        break  # Exit the loop if the password is correct
    else:
        print("Incorrect password.")
    if attempt == 4:  # On the last attempt (5th), inform the user
        print("Too many failed attempts. Access denied.")

# Explanation:
#     for attempt in range(5)::
#         This loop runs a maximum of 5 times, representing the 5 attempts the user has to enter the correct password.
#     password == "TiramisuinPizeria":
#         The code checks if the entered password matches the correct password "TiramisuinPizeria".
#     break:
#         If the password is correct, break exits the loop immediately, and the user is welcomed.
#     Handling Incorrect Attempts:
#         If the password is incorrect, the loop continues to prompt the user to try again.
#         After 5 failed attempts, the loop ends, and the user is informed that they have been denied access.