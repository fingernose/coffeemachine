
milk_used = int()
water_used = int()
coffee_used = int()
cost_price = float()
amount_paid = float()


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def rapport():
    """Create the report of the resources available"""
    return f" Water = {resources['water']}\n Milk = {resources['milk']}\n Coffee = {resources['coffee']}\n Money = ${resources['money']}"


def calcul(quart, dim, nick, penn):
    """Calcul the amount paid"""
    return (0.25 * quart + 0.10 * dim + 0.05 * nick + 0.01 * penn)


def check_resources():

    """This function checks if there is enough resources to prepare the command,
        and also checks if there is enough money"""

    if resources["water"] < MENU[client]["ingredients"]["water"]:
        return "Water"

    elif resources["coffee"] < MENU[client]["ingredients"]["coffee"]:
        return "coffee"

    elif resources["milk"] < MENU[client]["ingredients"]["milk"]:
        return "milk"
    else:
        return "OK"


def commande(client):
    """will take the user command"""
    if client == "espresso":
        MENU[client]["ingredients"]["milk"] = 0
    # TODO: Ajouter le calcul des ressources
    if check_resources() != "OK":
        print(f"Sorry, there is not enough {check_resources()}")

    else:
        print(f"The price for a {client} is: ${MENU[client]['cost']}, please insert coins: ")
        quarters = int(input("How many quarters ($0.25)? "))
        dimes = int(input("How many dimes ($0.10)? "))
        nickles = int(input("How many nickles ($0,05)? "))
        pennies = int(input("How many pennies ($0,01)? "))
        amount_paid = calcul(quart=quarters, dim=dimes, nick=nickles, penn=pennies)
        if amount_paid > MENU[client]['cost']:
            change = amount_paid - MENU[client]['cost']

            resources['money'] += (amount_paid - change)
            print(f"Here is your change ${round(change, 2)}")
            print(f"Enjoy your {client}")
            resources["water"] -= MENU[client]["ingredients"]["water"]
            resources["coffee"] -= MENU[client]["ingredients"]["coffee"]
            resources["milk"] -= MENU[client]["ingredients"]["milk"]
        elif amount_paid == MENU[client]['cost']:
            resources['money'] += amount_paid
            print(f"Enjoy your {client}")
        else:
            print(f"Sorry, that's not enough money, here is your {amount_paid}")

    #rapport()
# TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
"""”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
"""



# TODO: 3. Print report.
"""
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
"""
# will print the report or begin the command
machine_on = True
while machine_on:
    client = input("What would you like: Espresso ($1.50), Latte ($2.50) or Cappuccino ($3.00)? ").lower()

    if client == "report":
        print(rapport())
    elif client == "off":
        machine_on = False
    else:
        commande(client)



# calcul du montant




# TODO: 4. Check resources sufficient?
"""
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “ Sorry there is not enough water. ”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
"""





# TODO 5. . Process coins.
"""
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
"""

# TODO: 6. Check transaction successful?
"""
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “ Sorry that's not enough money. Money refunded. ”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change"""

# TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
"""
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
"""

