import math
from operator import truediv

full_name = "John Smith"
age = 20
is_new = True

name = input("What is your name " )
favorite_color = input("What color do you like ")
print(name + " likes "+ favorite_color)

# ask a user their weight(in pounds), convert it to kilograms and print on the terminal
weight = input("What is your weight ")
weight_in_kg =(int(weight) * 0.45)
print(f"Your weight is {weight_in_kg} kg")


#Strings in Python
course = "Python for Beginners"
another = course[:] #basically copies all the strings
print(course[1]) #gives the second index string
print(course[-1]) #gives the last string
print(course[0:6])
print(another)
print(course[0:-1]) #gives strings from 0 index upto the second last index


#Formatted Strings ---> how you print John [Smith] is a coder.
first_name = "John"
last_name = "Smith"
print(f"{first_name} [{last_name}] is a coder") #This is what you need to do, to print something like this

#String Methods
print(course.upper()) # all upper case
print(course.lower()) # all lower case
print(course.find('s')) # FIND provides the index of the s
print(course.find('o'))
print(course.find("Beginners"))
print("Python" in course) # IN provides boolean value--> in this case it's True
print(course.replace("Beginners", "Absolute Beginners"))
print(course) #But it doesn't change the string, the changes can be only seen in the code above
print(len(course)) #gives the length of the string


#Arithmetic Operations
print(10**3) #output is 1000
x = 5
x+=10
print(x) # results 15
x = 20
print(x) #the value of x will change to 20 at this point

#Math built in function
y = 2.9
print(round(y)) #rounds the value
print(abs(-2)) # always gives the positive value

#math module (similar to object) and accessing it's property
print(math.ceil(2.9))
print(math.floor(2.9))
print(math.erf(2.9)) #returns error function of a number
print(math.factorial(3))
print(math.fabs(-2.2))#returns absolute value of a number
print(math.fmod(4,2))
print(math.fsum([2,3,4,5,5]))#returns the sum of all items in tuples, array, lists, etc
print(int(math.pow(2,3)))#2to the power 3 which is 8, and getting it in a whole number with int()
print(math.sqrt(4))

#If statement
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
elif is_cold:
    print("It's a rainy day")
else:
    print('Enjoy your day')

house_price = 1000000
good_credit = True
gc_down = int((10/100) * house_price)
bc_down = int((20/100) *house_price)

if good_credit:
    print(f'You are putting just 10% down which is {gc_down}')

else:
    print(f'You are putting 20% down which is {bc_down}')

#LOGICAL OPERATORS  and or not >, <, <= ,>=, ==, !=
has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

elif has_high_income or has_good_credit:
    print("You are or operator")

else:
    print("You are not eligible for anything")

has_credit = True
has_criminal_record = False

if has_credit and not has_criminal_record:
    print("Printed this because it's true true")
else:
    print("You are in the else statement")


name = input("Enter your name ")
if len(name)<3:
    print("Name must be at least 3 characters")
elif len(name)>10:
    print("Name can be a maximum of 50 characters")
else:
    print("name looks good")

#Weight Converter Program
weight = int(input("Weight: "))
convention = input("(L)bs or (K)g: ")
pound_to_kg = weight * 0.45
kg_to_pound = weight * 2.20

if 'L' or 'l':
    print(f'You are {kg_to_pound} pounds')
elif 'K' or 'k':
    print(f'You are {pound_to_kg} kilograms')
else:
    print('Please enter write keyword to view your result')


#WHILE LOOP
num_first = 1
while num_first < 5:
    print(num_first)
    print("First Shahash " * num_first)
    num_first = num_first +1

#Guessing game with while loop

correct_guess = 9
looper = 1
while looper<4:
    guess = int(input("Guess: "))
    looper += 1
    if guess == correct_guess:
        print('You Win!')
        break
else:
    print('Sorry you failed')

#Project Building Car Game
command = ""
started = False
while command.lower() != "quit":
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car started")

    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = True
            print("Car is stopped")

    elif command == "quit":
        print("quit - to exit")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
""")
    elif command == "quit":
        break
    else:
        print("Sorry I don't understand")





