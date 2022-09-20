import re

items = {
"cheeseburger" : 2.50,
"fries" : 1.50,
"drink" : 1.00,
"dessert" : 1.50,
"pizza" : 3.00,
"salad" : 2.00,
"soup" : 1.50,
"sandwich" : 2.00,
"taco" : 1.50,
"burrito" : 2.00,
}

def lowercase_letters(string):
    """Converts all letters in a string to lowercase.

    Args:
        string (string): The input of the string you want to convert.

    Returns:
        string: returns the string with all letters converted to lowercase.
    """
    return re.sub('[^a-z]', '', string)


def check_exit(letter, phrase):
    """Checks if the user wants to exit the program.

    Args:
        letter (string): The letter that the user must enter to continue.
        phrase (string): The phrase that is printed to the user.

    Returns:
        boolean: returns True if the user enters the letter, False if not.
    """
    print(phrase)
    user_input = input()
    if user_input.startswith(letter):
        return True
    else:
        return False

def get_order():
    """Gets the order from the user.

    Returns:
        list: returns the order from the user.
    """
    order = ["", 0]

    script = "Items for sale:\n\n"
    for item in items:
        script += item + " - " + "${:,.2f}".format(items[item]) + "\n"

    print(script)

    actual_item = False
    while actual_item == False:
        item = input("What would you like to order? ")
        item = lowercase_letters(item)
        if item in items:
            actual_item = True
        else:
            print("Sorry, we don't have that item.")
    order[0] = item
    order[1] = items[item]
        

    return order

def print_order(orders):
    """Prints the order to the user.

    Args:
        orders (list): The list of orders.
    """
    print("Your orders include: \n")
    for item in orders:
        print(item[0] + " - " + "${:,.2f}".format(item[1]) + "\n")
    total = 0
    for item in orders:
        total += item[1]
    print("total: " + "${:,.2f}".format(total))

def get_tip(orders):
    """Gets the tip from the user.
    
    Args: orders (list): The list of orders.
    
    Returns: float: The tip from the user.
    """
    print_order(orders)
    total = 0
    for item in orders:
        total += item[1]
    print("Your total is: " + "${:,.2f}".format(total) + ", the suggested tip would be " + "${:,.2f}".format(total * 0.15))
    tip = 0
    while tip == 0:
        tip = float(input("How much would you like to tip? "))
        if tip < 0:
            return 0
        try:
            tip = float(tip)
        except:
            print("Please enter a number.")
            tip = 0
    return tip
        


def main():
    phrase = "Would you like to order something? (y/n) "
    letter = "y" # letter to exit
    orders = []

    if check_exit(letter, phrase):
        order = get_order()
        orders.append(order)
        print_order(orders)
        while (check_exit(letter, phrase)):
            order = get_order()
            orders.append(order)
            print_order(orders)
        else:
            print_order(orders)
            tip = get_tip(orders)
            total = 0
            for item in orders:
                total += item[1]
            print("Thank you for your order! Your tip is " \
                + "${:,.2f}".format(float(tip)) + " and your total is " \
                     + "${:,.2f}".format(float(tip) + total))
    else:
        print("Must enter " + letter + " to continue.")
        exit()

    return 0


if __name__ == "__main__":
    main()