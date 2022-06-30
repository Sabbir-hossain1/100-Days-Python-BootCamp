# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#from turtle import Turtle,Screen
#
# from prettytable import PrettyTable
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     # timmy = Turtle()
#     # timmy.shape("turtle")
#     # timmy.color("red", "coral")
#     # timmy.forward(200)
#     #
#     # myScreen = Screen()
#     # myScreen.canvheight
#     # myScreen.exitonclick()
#
#     table = PrettyTable()
#     table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
#     table.add_column("Type", ["Electric", "Water", "Fire"])
#     print(table)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True


while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



