from Menu import MENU,resources


def check_resources(Received_coffee_type,Received_MENU,Received_resources):
    """Returns True When order can be made, False if ingredients are insufficient"""
    
    if Received_coffee_type == "espresso":    
        if Received_MENU["espresso"]["ingredients"]["water"] > Received_resources["water"]:
            return "Sorry, Not enough Water"
        elif Received_MENU["espresso"]["ingredients"]["coffee"] > Received_resources["coffee"]:
            return "Sorry, Not enough Coffee"
        else:
            return True

        
        
    elif Received_coffee_type == "latte":
        if Received_MENU["latte"]["ingredients"]["water"] > Received_resources["water"]:
            return "Sorry, Not enough Water"
        
        elif Received_MENU["latte"]["ingredients"]["milk"] > Received_resources["milk"]:
            return "Sorry, Not enough milk"
        
        elif Received_MENU["latte"]["ingredients"]["coffee"] > Received_resources["coffee"]:
            return "Sorry, Not enough Coffee"
        else:
            return True
        
        
    elif Received_coffee_type == "cappuccino":
        if Received_MENU["cappuccino"]["ingredients"]["water"] > Received_resources["water"]:
            return "Sorry, Not enough Water"
        
        elif Received_MENU["cappuccino"]["ingredients"]["milk"] > Received_resources["milk"]:
            return "Sorry, Not enough milk"
        
        elif Received_MENU["cappuccino"]["ingredients"]["coffee"] > Received_resources["coffee"]:
            return "Sorry, Not enough Coffee"
        else:
            return True


total_input_money = 0
Money = 0
is_off = False

while not is_off:    
    coffee_type = input("What would you like ? (espresso/latte/cappuccino): ")
    resource_check = check_resources(coffee_type,MENU,resources)
    
    if coffee_type == "off":
        is_off = True
    elif coffee_type == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money : ${Money}")
        
    elif (coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino" ) and resource_check == True :
        print("Pleas Insert coins: ")
        total_input_mony = int(input("How many quarters? ")) * 0.25
        total_input_mony += int(input("How many dimes? ")) * 0.10
        total_input_mony += int(input("How many nickles? ")) * 0.05
        total_input_mony += int(input("How many pennies? ")) * 0.01
        
        if MENU[coffee_type]["cost"]<= total_input_mony:
            Money = Money + MENU[coffee_type]["cost"]
            if total_input_mony > MENU[coffee_type]["cost"]:
                extra_money = round((total_input_mony - MENU[coffee_type]["cost"]),2)
                
                resources['water'] = resources['water'] - MENU[coffee_type]["ingredients"]["water"]                            
                if coffee_type != "espresso":
                    resources['milk'] = resources['milk'] - MENU[coffee_type]["ingredients"]["milk"]
                    
                resources['coffee'] = resources['coffee'] - MENU[coffee_type]["ingredients"]["coffee"]
                
                
                print(f"Here is {extra_money} in change")
                print(f"Here is your {coffee_type} enjoy !")
            else:
                print(f"Here is your {coffee_type} enjoy !")
            
        else:
            "Sorry, Not enough Money"
            
    else:
        print(resource_check)
    
