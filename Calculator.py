# Calculator
from Calculator_art import logo
def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":sub,
    "*":mul,
    "/":div,    
    }

def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)
        
    should_continue = True
    
    while should_continue:    
        operation_symbol = input("Pick any symbol to perform calculation: ")
        num2 = float(input("Enter next number: ")) 
        operation = operations[operation_symbol]
        answer = operation(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"type 'y' to continue calculating {answer} or type 'n' to start a new calcuation: ")=="y":
            num1 = answer
        else:
            should_continue = False
            calculator()
        
calculator()
 