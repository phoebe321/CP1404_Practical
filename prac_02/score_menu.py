
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 70
PASSABLE_THRESHOLD = 50
menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """get user input and choice"""
    print(menu)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        score = float(input("Enter your score: "))
        if choice == "G":
            mark = get_valid_score(score)
            print(mark)
        elif choice == "P":
            grade = get_result(score)
            print(grade)
        elif choice == "S":
            display_asterisks(score)

        choice = input("Enter your choice: ").upper()
    print("farewell!")


def get_valid_score(score):
    """check user score"""
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter your score: "))
    return score


def get_result(score):
    """this function is to determine grade"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        message = "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        message = "Excellent"
    elif score >= PASSABLE_THRESHOLD:
        message = "Passable"
    else:
        message = "Bad"

    return message


def display_asterisks(score):
    """display asterisks according to the score"""
    print("*" * int(score))


main()
