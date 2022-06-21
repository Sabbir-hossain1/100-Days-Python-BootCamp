import string
import random

alphabet_string = string.ascii_lowercase
loweralphabet= list(alphabet_string)

alphabet_string = string.ascii_uppercase
Alphabets = list(alphabet_string)

Alphabets.extend(loweralphabet)
numbers = ['0','1','2','3','4','5','6','7','8','9']
sybmols = ['!','#','$','%','&','(',')','*','+']
password=""
passwordList = []

#Easy Level for password generation
"""
print("Welcome to the PyPassword Generator!")
numberOfLetters = int(input("How many letters would you like in your password ? \n"))
for i in range(0,numberOfLetters):
    password += Alphabets[random.randint(0,51)] # random.choice(Alphabets)
 
number_Symbols = int(input("How many symbols would you like ? \n"))
for i in range(0,number_Symbols):
    password += sybmols[random.randint(0,len(sybmols)-1)] # random.choice(sybmols)


number_numbers = int(input("How many numbers would you like ? \n"))
for i in range(0,number_numbers):
    password += numbers[random.randint(0,len(numbers)-1)] # random.choice(numbers)

print(password)
"""
#Hard Level for password generation
print("Welcome to the PyPassword Generator!")
numberOfLetters = int(input("How many letters would you like in your password ? \n"))
for i in range(0,numberOfLetters):
    passwordList.append(random.choice(Alphabets)) # Alphabets[random.randint(0,51)
 
number_Symbols = int(input("How many symbols would you like ? \n"))
for i in range(0,number_Symbols):
    passwordList.append(random.choice(sybmols)) 


number_numbers = int(input("How many numbers would you like ? \n"))
for i in range(0,number_numbers):
    passwordList.append(random.choice(numbers)) # random.choice(numbers)
 
random.shuffle(passwordList)
 
for i in passwordList:
    password +=i

print(password)


