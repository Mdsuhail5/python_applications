from day_16_menu_0 import Menu, MenuItem
from day_16_coffee_maker import CoffeeMaker
from day_16_money_machine import MoneyMachine
is_machine_off = False
rep = CoffeeMaker()
menu = Menu()
money = MoneyMachine()
while not is_machine_off:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == 'off':
        is_machine_off = True
    elif choice == "report":
        rep.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if rep.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            rep.make_coffee(drink)
