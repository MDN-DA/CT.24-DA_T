print("What is the capital of England")
answer = input("The capital of England: ndon")

if answer == "London" or answer.lower() == "london":
    print(f"Correct! the answer is {answer}.")
else:
    print(f"Incorrect, the answer is 'London', not {answer}.")