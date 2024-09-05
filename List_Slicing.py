l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#[start:end:stride]
#start--> inclusive, end: exclusive, stride: every other in case of 2
print (l[2:9:2])

#To retrive every odd elements from the list given below
my_list = range(1, 11) # List of numbers 1 - 10

# Add your code below!
print(my_list[1::2])


#Reversing a list using the stride -1
my_list = list(range(1, 11))
print(my_list)
# Add your code below!
backwards = my_list[::-1]
print(backwards)