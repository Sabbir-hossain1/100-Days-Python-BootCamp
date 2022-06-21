print("Welcome to Treassure Island")
print("Your mission is to find the Treasure")
left_right = (input("left or right ")).lower()
if left_right=="left":
    swim_wait = (input("Do you want to swim or wait for boat ")).lower()
    if swim_wait=="wait":
        door = (input("Which Door do you want to go? ")).lower()
        if door == "yellow":
            print("You win")
        else:
            print("Game over")
    else:
        print("Game Over")
else:
    print("Game Over")