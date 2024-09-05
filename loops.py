import math
import random
num = 1
while num < 11:
    result = math.pow(num, 2)
    print(result)
    num+= 1


# while with if and else -----> watch the program flow
print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
    num = random.randint(1, 6)
    print(num)

    if num == 5:
        print("Sorry, you lose!")
        break
    count+= 1
else:
  print("You win!")

# Check this program
#Let's you play the game until the count is greater than 0 on right guess program breaks with the "you win message" otherwise let's you
# play again for upto 3 times max, if you can't guess the correct number then you will see "you lose" message
from random import randint
guesses_left = 3
random_number = randint(1, 10)
print(f"This will print the random number and the random number is {random_number}")

while guesses_left > 0:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print("You win!")
        break
    guesses_left -= 1
else:
    print("You lose.")


#Another program that FOR loop has the most application of that is in the LIST, could use range as well, visualize the difference
numbers  = [7, 9, 12, 54, 99]

print ("This list contains: ")

for num in range(len(numbers)):
  print(numbers[num])

# Add your loop below!
for item in numbers:
  item = item **2
  print(item)

#Another example of FOR LOOP
choices = ['pizza', 'pasta', 'salad', 'nachos']

print ('Your choices are:')
for index, item in enumerate(choices):
  print (index + 1, item)


#FOR LOOP in the two lists, zip is the built in function
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    print( max(a, b))

# For loops with else statement  ---> check the indentation, else will only work if the break doesn't execute
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print ('You have...')
for f in fruits:
  if f == 'tomato':
    print ('A tomato is not a fruit!')
    break
  print ('A', f)
else:
  print ('A fine selection of fruits!')

def is_int(x):
  x = float(x)
  if x.is_integer():
      return True
  else:
      return False

print(is_int(5))

#Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number’s digits.
# For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4. (Assume that the number you are given will always be positive.)

def digit_sum(n):
    total =0
    value_n = str(n)
    for char in value_n:
        total = total + int(char)
    return total
print(digit_sum(1234))

#.Define a function factorial that takes an integer x as input.
#Calculate and return the factorial of that number.
def factorial1(x):
    total = 1
    for i in range(1,x+1):
        total = total * i
    return total
#Any of these functions work
def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x-1)

print(factorial(5))

