# Portfolio assignment 1
# Beckett pizza parlour price calculator

# Function to calculate total price of pizza order
def price_calculator():
    p_price = 12

    # If it is a Tuesday, all pizza is 50% off
    from datetime import datetime
    now = datetime.now()
    if now.strftime("%A") == "Tuesday":
        print("It's Tuesday! All pizzas are 50% off!")
        p_price = p_price / 2
    else:
        day = now.strftime("%A")
        print(f"Today is {day}. Pizza will remain at full price.")

    valid = False
    while not valid:
        pizzas_ordered = input('How many pizzas ordered?\n')
        if pizzas_ordered.isnumeric():
            if int(pizzas_ordered) > 0:
                valid = True
            else:
                print(f'Please enter a number above 0. {pizzas_ordered} is not above 0.')
        else:
            print(f'{pizzas_ordered} is not a valid input. Please enter a valid number.')

    pizzas_ordered = int(pizzas_ordered)

    valid = False
    while not valid:
        delivery = input('Is delivery required?\n')
        if delivery.lower() == "yes" or delivery.lower() == "no":
            valid = True
        else:
            print(f"{delivery} is not a valid input. Please enter either 'yes' or 'no'.")
    if delivery.lower() == "yes":
        if pizzas_ordered >= 5:
            d_price = 0
        else:
            d_price = 2.5
    else:
        d_price = 0

    valid = False
    while not valid:
        app = input('Did the customer use the app?\n')
        if app.lower() == "yes" or app.lower() == "no":
            valid = True
        else:
            print(f'{app} is not a valid input. Please enter either "yes" or "no".')

    # Calculating total price
    total = (pizzas_ordered * p_price) + d_price
    total = round(total, 2)
    if app.lower() == "yes":
        total = total * 0.75
        print(f'The total price is £{total}')
    else:
        print(f'The total price is £{total}')


price_calculator()
