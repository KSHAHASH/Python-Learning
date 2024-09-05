#Program to check the even numbers
def is_prime(x):
    if x < 2:
        return False
    for n in range(2, x - 1):
        if x % n == 0:
            return False
    else:
        return True

print(is_prime(13))
print(is_prime(10))

def reader(text):
    for item in text:




