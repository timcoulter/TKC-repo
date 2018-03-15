def main():
    score = get_score()
    if score in range(0,101):
        if score >= 90:
            print("Excellent")
        elif score >= 50:
                print("Passable")
        elif score < 50:
            print("Bad")
    else:
        print("Invalid score")
def get_score():
    while True:
        try:
            score = float(input("Enter your score here: "))
            break
        except ValueError:
            print("Score must equal a number between 0 and 100")
            score = float(input("Enter your score here: "))
    return score
main()
