import math
print("---------------------Welcome to prime Checker--------------\n")

n = int(input("Enter the number: "))

def prime_checker(number):
    sqr = int(math.sqrt(number))+1
    prime_flag = True    
    for i in range(2,sqr):
        if number % i == 0:
            prime_flag = False
            
    if prime_flag == True:
        print("It is a Prime Number")
    else:
        print("Not prime")
        
prime_checker(number = n)