import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_score(card_list):
#     if 11 in card_list and 10 in card_list and len(card_list) == 2:
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)

def compare_score(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has a BlackJack"
    elif user_score == 0:
        return "Win with a BlackJack"
    elif user_score > 21 :
        return "You went over.You lose"
    elif computer_score > 21 :
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return("you win")
    else:
        return "You lose"


user_card = []
computer_card = []
is_game_over = False

for _ in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())
while not is_game_over:    
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    print(f"Your card: {user_card}, current Score: {user_score}")
    print(f"Computer's first card: {computer_card[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_card.append(deal_card())
        else:
            is_game_end = True
while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computed_score = calculate_score(computer_card)
    
print(compare_score(user_score,computer_score))
