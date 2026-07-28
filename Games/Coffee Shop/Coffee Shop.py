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
}

def resourceCheck(orderIngredients):
    for item in orderIngredients:
        if orderIngredients[item] > resources[item]:
            print(f"Sorry There Is Not Enough Item. ({item})")
            return False
        else:
            return True

print("Price List: Espresso = $1.5, Latte = $2.5, Cappuccino = $3.")

def insertCoins():
    print("Please Insert Coins: ")
    total = int(input("Quarters: ")) * 0.25
    total += int(input("Dimes: ")) * 0.1
    total += int(input("Nickel: ")) * 0.05
    total += int(input("Pennies: ")) * 0.01
    return total

profit = 0

def transaction(moneyReceived, drinkCost):
    if moneyReceived >= drinkCost:
        change = round(moneyReceived - drinkCost, 2)
        print(f"Here Is Your Change: ${change}")
        global profit
        profit += drinkCost
        return True
    else:
        print("That's Not Enough Money!")
        return False

def makeCoffee(drinkName, orderIngredients):
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]
    print(f"Here Is Your '{drinkName}' ☕️.")

isOn = True

while isOn:
    choice = input("What Would You Like (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        isOn = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if resourceCheck(drink["ingredients"]):
            payment = insertCoins()
            if transaction(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])