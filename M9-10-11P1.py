total_ext_price = 0

def compute_total(qty, price):
    total = qty * price

    if total > 10000:
        total = total * 0.90

    return total

while True:
    qty = input("Enter quantity (or X to quit): ")

    if qty.upper() == "X":
        break

    qty = float(qty)
    price = float(input("Enter unit price: "))

    ext_price = compute_total(qty, price)

    total_ext_price += ext_price

    print(f"Quantity: {qty}")
    print(f"Price: ${price:.2f}")
    print(f"Extended Price: ${ext_price:.2f}")
    print()

print(f"Total Extended Price: ${total_ext_price:.2f}")


# More Functions Problem 1 - Sales Forecast

def forecast_sales(month, sales):

    month = month.lower()

    if month in ["jan", "feb", "mar"]:
        percent = 0.10
    elif month in ["apr", "may", "jun"]:
        percent = 0.15
    elif month in ["jul", "aug", "sep"]:
        percent = 0.20
    else:
        percent = 0.25

    next_month_sales = sales * (1 + percent)

    return next_month_sales

while True:
    choice = input("Do you want to continue? (Yes or No): ")

    if choice.lower() != "yes":
        break

    lastname = input("Enter last name: ")
    month = input("Enter month (Jan-Dec): ")
    sales = float(input("Enter sales amount: "))

    forecast = forecast_sales(month, sales)

    print(f"Last Name: {lastname}")
    print(f"Forecast Sales: ${forecast:.2f}")
    print()


# Advanced Functions Problem 1 - Discount Amount and Discounted Price

def compute_discount(qty, price, discount_rate):

    total = qty * price

    discount_amount = total * discount_rate

    discounted_price = total - discount_amount

    return discount_amount, discounted_price

while True:
    qty = input("Enter quantity (or X to quit): ")

    if qty.upper() == "X":
        break

    qty = float(qty)
    price = float(input("Enter price: "))
    discount_rate = float(input("Enter discount rate (example .10): "))

    discount_amount, discounted_price = compute_discount(
        qty, price, discount_rate
    )

    print(f"Quantity: {qty}")
    print(f"Price: ${price:.2f}")
    print(f"Discount Amount: ${discount_amount:.2f}")
    print(f"Discounted Price: ${discounted_price:.2f}")
    print()
