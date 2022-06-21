import random
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))
computer = random.randint(0,2)

if choose == 0 and computer == 2:
    print(f"Computer choice {computer} and Your choice {choose}")
    print("You win")
elif choose == 1 and computer == 0:
    print(f"Computer choice {computer} and Your choice {choose}")
    print("You win")
elif choose == 2 and computer == 1:
    print(f"Computer choice {computer} and Your choice {choose}")
    print("You win")
else:
    print(f"Computer choice {computer} and Your choice {choose}")
    print("You fail")