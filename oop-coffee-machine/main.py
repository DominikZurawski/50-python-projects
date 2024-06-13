from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_express = CoffeeMaker()
express_money = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    command = input(f"What would you like? ({menu.get_items()}): ")
    if command == 'off':
        is_on = False
    elif command == 'report':
        coffee_express.report()
        express_money.report()
    else:
        drink = menu.find_drink(command)
        if coffee_express.is_resource_sufficient(drink):
            if express_money.make_payment(drink.cost):
                coffee_express.make_coffee(drink)