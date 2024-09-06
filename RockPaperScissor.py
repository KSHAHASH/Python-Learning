#Rock paper and scissor game
from random import random
import random

user_value = input("Please enter either r, p, s: ").lower()
computer_value = random.choice(['r','p','s'])

def scissor_game():
    print(computer_value)
    if user_value == computer_value:
        print("Game is tie")

    elif (user_value == 'r' and computer_value == 's') or (user_value == 's' and computer_value == 'p')\
        or  (user_value == 'r' and computer_value == 's'):
        print("You won!")
    else:
        print("You lost")

scissor_game()

