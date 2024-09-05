def anti_vowel(text):
    words = ""
    vowels_text = ["a",'e',"i",'o','u']
    for char in text:
        if char.lower() not in vowels_text:
            words = words + char
        else:
            print(f"Printed character {char}")
    return  "".join(words.split()) #if you want to join the string
print(anti_vowel("i am from neEpal"))

