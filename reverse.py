def reversing_string(text):
    word = ""
    length_of_string = len(text)-1
    for char in text:
        word = word + text[length_of_string]
        length_of_string-=1
    return word
print(reversing_string("KATHMANDUU"))