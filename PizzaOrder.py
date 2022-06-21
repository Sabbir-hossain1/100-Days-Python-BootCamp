print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size=="s":
    price = 15
    if add_pepperoni=="y":
        price +=2
    if extra_cheese=="y":
        price +=1
elif size=="m":    
    price=20
    if add_pepperoni=="y":
        price +=3
    if extra_cheese=="y":
        price +=1
else:
    price =25
    if add_pepperoni == "y":
        price +=3
    if extra_cheese=="y":
        price +=1
print(f"Your final bill is : ${price}.")

