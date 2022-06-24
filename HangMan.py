#Step 1 
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
lives = 6

for index in range(0,len(chosen_word)):
    display.append("_")
print(display)

end_of_game = False
while  not end_of_game:
    guess = input("Guess a letter: ").lower()

    for index in range(0,len(chosen_word)):
        letter = chosen_word[index]
        if letter == guess:
            display[index] = letter
    print(display)       
    if guess not in chosen_word:
        lives -=1
        if lives == 0:
            end_of_game = True
            print("You lose")
    
    if "_" not in display:
        end_of_game = True
        print("You win")
    print(stages[lives])
        

