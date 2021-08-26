# A program that converts digits to words
from module import *


# FUNCTIONS GOES HERE

def decision(number):
    choice = decide(number)
    value = choice(number)
    return value


# PROGRAM IS RUN AT THIS POINT
print("A program that converts your digits to words. Type exit when done.")
currency = input("Enter currency: ")
while True:
    user_input = input("Enter numbers: ")
    if user_input == "exit":
        break
    x = decision(user_input)
    print(f'{user_input} = {x} {currency}')
