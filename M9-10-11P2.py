player_count = 0

def batting_average(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats

while True:
    lastname = input("Enter player last name (or X to quit): ")

    if lastname.upper() == "X":
        break

    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))

    average = batting_average(hits, at_bats)

    player_count += 1

    print(f"Player: {lastname}")
    print(f"Batting Average: {average:.3f}")
    print()

print(f"Total Players Entered: {player_count}")

# More Functions Problem 2 - Automobile Sales

total_msrp = 0
total_sales_price = 0

def compute_price(msrp, make, model, electric):

    if electric.upper() == "Y":
        discount = 0.30
    elif make.lower() == "honda" and model.lower() == "accord":
        discount = 0.10
    elif make.lower() == "toyota" and model.lower() == "rav4":
        discount = 0.15
    else:
        discount = 0.05

    new_price = msrp - (msrp * discount)

    sales_tax = new_price * 0.07

    total_price = new_price + sales_tax

    return total_price

while True:
    choice = input("Do you want to continue? (Yes or No): ")

    if choice.lower() != "yes":
        break

    make = input("Enter make: ")
    model = input("Enter model: ")
    electric = input("Electric vehicle? (Y or N): ")
    msrp = float(input("Enter MSRP: "))

    final_price = compute_price(msrp, make, model, electric)

    total_msrp += msrp
    total_sales_price += final_price

    print(f"Make: {make}")
    print(f"Model: {model}")
    print(f"Final Price: ${final_price:.2f}")
    print()

print(f"Total MSRP: ${total_msrp:.2f}")
print(f"Total Sales Price: ${total_sales_price:.2f}")

# Advanced Functions Problem 2 - Student Scores

def compute_scores(score1, score2, score3):

    total_points = score1 + score2 + score3

    average = total_points / 3

    return total_points, average

while True:
    lastname = input("Enter student last name (or X to quit): ")

    if lastname.upper() == "X":
        break

    score1 = float(input("Enter exam score 1: "))
    score2 = float(input("Enter exam score 2: "))
    score3 = float(input("Enter exam score 3: "))

    total, average = compute_scores(score1, score2, score3)

    print(f"Student: {lastname}")
    print(f"Total Points: {total:.2f}")
    print(f"Average Score: {average:.2f}")
    print()
