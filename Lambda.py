#USE OF LAMBDA


my_list = list(range(16))
print (filter(lambda x: x % 3 == 0, my_list))


#USE OF LAMBDA
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print(list(filter(lambda x: x == "Python", languages)))

#Create a list, squares, that consists of the squares of the numbers 1 to 10. A list comprehension could be useful here!
#Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).
squares = [x ** 2 for x in range(1, 11)]
filtered_squares = list(filter(lambda x: x >= 30 and x <= 70, squares))
print(filtered_squares)

#Filtering out the X from the expression below
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = "".join(filter(lambda x: x !='X', garbled))
print(message)