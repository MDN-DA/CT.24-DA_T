import random
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)

work_quotes = [
    "Choose a job you love, and you will never have to work a day in your life. — Confucius",
    "Success usually comes to those who are too busy to be looking for it. — Henry David Thoreau",
    "The only way to do great work is to love what you do. — Steve Jobs",
    "Hard work beats talent when talent doesn’t work hard. — Tim Notke",
    "Do not whine... Do not complain. Work harder. Spend more time alone. — Joan Didion"
]
health_quotes = [
    "Take care of your body. It’s the only place you have to live. — Jim Rohn",
    "Health is the crown on the well person’s head that only the ill person can see. — Robin Sharma",
    "A healthy outside starts from the inside. — Robert Urich",
    "The greatest wealth is health. — Virgil",
    "Health is not valued till sickness comes. — Thomas Fuller"
]
fun_quotes = [
    "In every job that must be done, there is an element of fun. — Mary Poppins",
    "People rarely succeed unless they have fun in what they are doing. — Dale Carnegie",
    "It’s kind of fun to do the impossible. — Walt Disney",
    "Fun is one of the most important—and underrated—ingredients in any successful venture. — Richard Branson",
    "The most wasted of all days is one without laughter. — E.E. Cummings"
]

def display_quote():
    print("Pick a category: work, health, or fun")
    choice = input("Your choice: ")
    if choice == "work":
        print(Fore.GREEN + random.choice(work_quotes))
    elif choice == "health":
        print(Fore.BLUE + random.choice(health_quotes))
    elif choice == "fun":
        print(Fore.YELLOW + random.choice(fun_quotes))
    else:
        print(Fore.RED + "Try again! - Please choose between work, health or fun.")

display_quote()
