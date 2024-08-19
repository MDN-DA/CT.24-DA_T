# def say_hello():
#     print("COYG")
# def account():
#     print("Starling Bank")

# account()
# say_hello()
# account()

# def abba(something):
#     print(f"{something}")

# abba("Hello Everyone")
# abba("Feed the fish")

balance = 2350
def cash_withdrawal(amount, acc_num):
    global balance
    print(f"You have {balance} in your account")
    print(f"Withdrawing {amount} from account number: {acc_num}")
    balance = (balance-amount)
    print(f"Your new balance is {balance}")

cash_withdrawal(350, 28564091)
cash_withdrawal(120, 56437754)