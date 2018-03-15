def main():
    score = get_score()
    if score not in range(0, 101):
        print("Invalid")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def get_score():
    while True:
        try:
            score = int(input("Enter an integer score between 0 and 100 here: "))
            break
        except ValueError:
            score = int(input("Enter an integer score between 0 and 100 here: "))
    return score

main()

