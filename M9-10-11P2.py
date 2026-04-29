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
