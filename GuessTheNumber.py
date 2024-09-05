#Guess The Number Game
# I am going to guess the number and see if that number is the random number
#if it is then I am going to indicate that I won the game otherwise you get to try until you guess it correctly
# best approach is to create a function and pass the argument as a guess
import random

def guess():
    random_number = int(random.randint(1, 10))
    # you have to pass something so that the loops run, since 0 is not inside the random number it is the perfect number
    guess_number = 0
    while random_number!= guess_number:
        #print(random_number)
        guess_number = int(input("Please enter your guess: "))
        if guess_number > random_number:
            print(f"You number is greater than the random number")
        elif guess_number < random_number:
            print(f"your number is less than the random number")
    print(f"Yay! your guess is correct!!!")

guess()






