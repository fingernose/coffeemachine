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

rapport_produit = str()

# TODO: 1. prompt user: What would you like
# TODO: 2. prompt user to pay
# Espresso, latte or Capuccino
user = input("What would you like: Espresso ($1.50), Latte ($2.50) or Capuccino ($3.00)? ").lower()
print(f"The price for a {user} is: ${MENU[user]['cost']}, please insert coins: ")
quarters = int(input("How many quarters ($0.25)? "))
dimes = int(input("How many dimes ($0.10)? "))
nickles = int(input("How many nickles ($0,05)? "))
pennies = int(input("How many pennies ($0,01)? "))

# calcul du montant
def calcul(quart, dim, nick, penn):
    return (0.25 * quart) + (0.10 * dim) + (0.05 * nick) + (0.01 * penn)


print(calcul(quarters, dimes, nickles, pennies))
# TODO: 3. Print report
def report(a):
    return f"{a} = {resources[a]}"


print(report("water"))


# TODO: 5. Check resources sufficient and payment
def check_resources():
    """This function checks if there is enough resources to prepare the command,
    and also checks if there is enough money"""




# TODO 4. Enlever les ressources utilisees par la commande


# TODO 5. E
# TODO: 5. Process coins

# TODO: 6. Check transactions is successful

# TODO: 2. Turn off the coffee machine
