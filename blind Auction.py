import os
bidding_dictionary = {}
bidding_finish = False


def find_height_bidder(bidding_record):
    highest_bidding_amount=0
    winner = ""
    
    for bidder in bidding_record:
        bidding_amount = bidding_record[bidder]
        if(bidding_amount > highest_bidding_amount):
            highest_bidding_amount = bidding_amount
            winner = bidder
            
    print(f"Thw winner is {winner} with a bid of ${highest_bidding_amount}")

while not bidding_finish:
    name = input("What is your name? ")
    bid_price = int(input("your bidding price ? "))
    bidding_dictionary[name] = bid_price
    should_continue = input("Are there any bidders? Type 'yes' or 'no' ")
    if should_continue == "no":
        bidding_finish = True
        find_height_bidder(bidding_dictionary)
    elif should_continue == "yes":
        os.system('cls')
         
        


