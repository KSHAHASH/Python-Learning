#For loops in Python
from operator import index

for item in 'Shahash':
    print(item)

result =0
for item1 in range(10):
    result = result + item1
print(result)

for item2 in range(5,10):
    print(item2)

#sum in the LIST
prices = [1,2,3,4,5]
total =0
for price in prices: #price is kind of i
    total = total + price
print(f'The total is {total}')


#Nested Loops ---> useful for getting co ordinates
for i in range(2):
    for j in range(2):
        print(f'({i},{j})')

numbers = [5,2,5,2,2]
for i in numbers:
    print(f'{i}')

names = ["shahsash", "kandel", "sagaramtha","himal","banana"]
print(names[0])
print(names[2:])
print(names)
names[0] = "shahash"
print(names) #it would give the new array with the first index value correct unlike line 33

#Write a program to find the largest number in a list
numbers = [3,6,2,4,10,8]
largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print(largest)

#2D LIST
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[2][1])
print(matrix[2][1], matrix[2][2])

#Lists

numbers = [1,2,3,4,5,6]
numbers.append(66)
numbers.insert(0,5)
numbers.remove(4)
numbers.pop() #delete the last element of the list
print(numbers)
print(index(5))
print(numbers.count(5)) #counts number of 5 in the list
numbers.sort() #sorts the list in ascending order
numbers.reverse() # sorts in the descending order
number2 = numbers.copy() #to copy the list into another variable
print(number2)
print(numbers)

#Write a program to remove the duplicates in a list

values = [1, 5, 7, 5, 6 , 7, 8]
uniques = []

for value in values:
    if value not in uniques:
        uniques.append(value)
print(uniques)

#Tuples  --> similar to the list but cannot mutate it
shahash = (22,33,44,55)
print(shahash[0])

#Unpacking in Python can be used with the LIST as well as with TUPLES -> useful for co-ordinates
coordinates = (1,2,3)
x,y,z = coordinates
print(x,y,z)

#Dictionaries in Python
dictionaries ={
    "name": "Shhaash",
    "age": 23,
    "is_verifed": True
}

print(dictionaries["name"]) #to access the key value pair
dictionaries["place"] = "Nepal" # to add the property inside the dictionary
dictionaries.get("new_place", "Pokhara")
dictionaries["name"] = "kandel" # to mutate the value of the key
print(dictionaries)

hello = input("Phone: ")
phone = {
    "1": "one ",
    "2": "two ",
    "3": "three ",
    "4": "four"
}

output = ""
for value in hello:
    output+= phone[value] + ""
print(output)

def square(n):
    """Returns the square of a number."""
    squared = n ** 2
    print(f"{n} squared is {squared} ")

square(10)


def biggest_number(*args):
    return max(args)
biggest = biggest_number(-10, -5, 5, 10)
print (f"Biggest number is {biggest}")

def hotel_cost(nights):
  return print(140 * nights)

print(hotel_cost(3))

#Counting the number of times "fizz" has been repeated in a list using the function and the for loop
def fizz_count(items):
    times_repeated = 0
    for item_1 in items:
        if item_1 == "fizz":
            times_repeated += 1
    return times_repeated


fizz = ["fizz", "shahasha", "fizz"]
handler = fizz_count(fizz)
print(handler)

#Dictionary and accessing the keys and values using the for loop
#Since they have same keys so we can just loop through any of the dictionary
stock =  {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}

price={
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

for values in stock:
    print(f"{values}:")
    print(f"stock: {stock[values]}")
    print(f"price: {price[values]}")

# look at this carefully we want to get the total inventory by multiplying the stock and prices and getting total of it
total_inventory = 0
for key in stock:
    initial_value = stock[key] * price[key]
    print(initial_value)
    total_inventory+= initial_value
print(total_inventory)

num_one = [1,3,4,5,56,6]
another= sum(num_one)
print(another)

#Very Good example of Function that clarifies everything from the python 2 codeacademy
lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):
  homework = average(student["homework"])
  quizzes = average(student["quizzes"])
  tests = average(student["tests"])
  return 0.1 * homework + 0.3 * quizzes + 0.6 * tests

def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >=80:
    return "B"
  elif score >=70:
    return "C"
  elif score >=60:
    return "D"
  else:
    return "F"

def get_class_average(class_list):
  results = []
  for student in class_list:
    student_avg = get_average(student)
    results.append(student_avg)
  return average(results)

students = [lloyd, alice, tyler]

avg = get_class_average(students)
print(avg)
print(get_letter_grade(avg))

#Removing the items from the list
#you can use remove--->list_name.remove(actual_item), list_name.pop(index), del(list_name[index])
fruits = ['apple','banana', "grapes","papaya","blueberry"]
fruits.remove("apple")
print(fruits)
fruits.pop(2)
print(fruits)
del(fruits[1])
print(fruits)

#Range Example similar to the for loop starting from index 0 to length of the array in the javascript
#NOTE----->Simple for loop without range is just used to print the list elements whereas with range we could modify the list
n = [3, 5, 7]
def double_list(x):
    for items in range(0,len(x)):
        x[items] = x[items]+1
        return x

print(double_list(n))

#Joining two lists together from a function using as a argument
m = [1, 2, 3]
n = [4, 5, 6]

def joiner_list(a,b):
    result_list =[]
    result_list.append(m)
    result_list.append(n)
    return result_list
print(joiner_list(m,n))

#NOTE----->To concatenate you have to use "+" sign

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in range(0, len(lists)):
        results.append(lists[numbers])
    return results

print (flatten(n))  # result will be [[1, 2, 3], [4, 5, 6, 7, 8, 9]] but that's not what we want we want them in one list

# This will be the code that will flatten the list
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
def flattened(lists):
  results = []
  for numbers_1 in lists:
    print (numbers_1)
    for number_1 in numbers_1:
      print (number_1)
      results.append(number_1)
  return results

print (flattened(n))  # This will print [1,3,4,5,6,7,8,9]
print (flattened(n))  # This will print [1,3,4,5,6,7,8,9]