import random
from HigherLowerArt import logo,vs
from higher_lower_game_data import data

A = random.choice(data)
B = random.choice(data)
score = 0 


should_continue = False
print(logo)

while not should_continue:
    
    print(f"Current Score: {score}")
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}. {A['follower_count']}")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}. {B['follower_count']}")
    followers = input("Who has more followers? Type 'A' or 'B': ")
    print("\n")
    if followers == "a" :
        if A['follower_count'] > B['follower_count']:
            score = score + 1
        else:
            print(f"Sorry, that's worng. Final score: {score}")
            should_continue = True
            
    elif followers == "B":
        if B['follower_count'] > A['follower_count']:
            score = score + 1
        else:
            print(f"Sorry, that's worng. Final score: {score}")
            should_continue = True
    A = B
    B = random.choice(data)
    if A['name'] == B['name']:
        B = random.choice(data)

