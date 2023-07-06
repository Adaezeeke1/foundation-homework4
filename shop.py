#Final changes for pull request
items = {
    'apple': 1.50,
    'banana': 0.75,
    'bread': 3.99,
    'cheese': 8.99,
    'kiwi': 6.40,
    'mango': 5.99,
    'milk': 10.00,
    'orange': 7.30,
    'red wine': 150.00,
    'yoghurt': 10.50
}

available_money = 100.00
max_purchase_attempts = 3


class MaximumPurchaseAttemptsExceededError(Exception):
    pass


def display_items():
    print("Items available for purchase:")
    for item, price in items.items():
        print(f"{item}: £{price:.2f}")


def make_purchase(option):
    global available_money
    if option.lower() == 'exit':
        print("Thank you for visiting the shop. Goodbye!")
        return True

    if option not in items:
        raise ValueError("Invalid item.")

    price = items[option]
    if price <= available_money:
        available_money -= price
        print(f"Here's your {option}!")
        print(f"Your available money now is £{available_money:.2f}")
        print("Thank you for shopping with us. Goodbye!")
        return True

    return False


def add_money():
    additional_money = float(input("You don't have enough money. Do you have more money? Enter the amount: "))
    return additional_money


def shop():
    global available_money
    print("Welcome to the shop!")
    display_items()
    print("Enter 'exit' to leave the shop.")

    purchase_attempts = 0
    while purchase_attempts < max_purchase_attempts:
        try:
            option = input("Enter the item you want to purchase: ")
            if make_purchase(option):
                break

            additional_money = add_money()
            available_money += additional_money
            print(f"Your available money now is £{available_money:.2f}")
            purchase_attempts += 1

        except ValueError:
            print("Invalid input. Please try again.")

        except MaximumPurchaseAttemptsExceededError:
            print("Maximum purchase attempts exceeded. You cannot make any more purchases.")
            break

    if purchase_attempts == max_purchase_attempts:
        raise MaximumPurchaseAttemptsExceededError


shop()
