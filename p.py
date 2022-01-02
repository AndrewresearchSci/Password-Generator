import random

print("Welcome to password Generator")

Rint = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@!#$%£_"

numbers = input('The amount of passwords to generate: ')
numbers = int(numbers)

length = input('The Length of these passwords that you would like to generate: ')
length = int(length)

for p in range(numbers):
    password = ''
    for c in range(length):
        password += random.choice(Rint)

    print(password)

    print("The End")
