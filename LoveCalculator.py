print("Welcome to the love calculator")
name1 = (input("What is your name ? ")).lower()
name2 = (input("What is your partner name? ")).lower()
print(name1+" "+name2)
partner1 =0;
partner2 =0;
partner1 += name1.count('t')
partner1 += name1.count('r')
partner1 += name1.count('u')
partner1 += name1.count('e')

partner1 += name1.count('l')
partner1 += name1.count('o')
partner1 += name1.count('v')
partner1 += name1.count('e')
print(f"Partner1 Score is {partner1}")

partner2 += name2.count('t')
partner2 += name2.count('r')
partner2 += name2.count('u')
partner2 += name2.count('e')

partner2 += name2.count('l')
partner2 += name2.count('o')
partner2 += name2.count('v')
partner2 += name2.count('e')
print(f"Partner2 Score is {partner2}")

finalScore = partner1+partner2*10
print(finalScore)
if finalScore<10 and finalScore>90:
    print(f"Your score is {finalScore}, you go togther like coke and mentos.")
elif finalScore<=40 and finalScore>=50:
    print(f"Your score is {finalScore}, you are alright together.")
else:
    print(f"Your score is {finalScore}.")



