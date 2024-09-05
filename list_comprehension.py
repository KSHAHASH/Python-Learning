#List Comprehension
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print (evens_to_50)

#Your even_squares list should include the squares of the even numbers between 1 to 11.
# Your list should start [4, 16, 36...] and go from there.
even_squares = [item **2 for item in range(1, 11) if(item **2)%2 == 0]
print (even_squares)

#Prints [c, c, c]
c = ['C' for x in range(5) if x < 3]
print (c)

#Justing making sure to print the values of the nested list in a single list
values = [[1,2,4,5],[5,6,7,8]]
def appender(value_1):
    result = []
    for item in values:
        for item_1 in item:
            print(item_1)
            result.append(item_1)
    return result
print(appender(values))