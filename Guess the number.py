import random
print("Welcome to the number Guessing Game !")
print("I am thinking of a number between 1 and 100 ")
Difficulty_type = input("Choose a difficulty. Type 'easy' or 'hard': ")
if Difficulty_type == 'easy':
    life = 10
elif Difficulty_type == 'hard':
    life = 5
Random_number = random.randint(1,100)
while life != 0:
    print(f"You have {life} life attempt to guess the number.")
    guess = int(input("Make a guess: "))
    
    if Random_number > guess :
        print("low guess \n guess again")
    elif Random_number < guess:
        print("High guess \n Guess again")
    elif Random_number == guess:
        print("Your guess is correct.")        
        break
    life = life - 1    
if life == 0:
    print("You've run out of guess, you lose.")