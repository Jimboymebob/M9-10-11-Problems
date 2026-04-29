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
