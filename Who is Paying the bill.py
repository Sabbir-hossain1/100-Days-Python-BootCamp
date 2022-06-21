import random
name_string = input("Give me everybody's names seperated by a comma. ")
names = name_string.split(", ") #make a list from the given name string
biller_index = random.randint(0,len(names)-1) #find random index to pay the bill
print(names[biller_index]) #Random bill payer names

# Radom choise also can be done by
# random_names = random.choice(names)
# print(random_names)
 