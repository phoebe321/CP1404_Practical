
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOULD = 90
PASSABLE_THRESHOULD = 50


import random


def main():
    """get user input"""
    user_score = int(input("Enter your score: "))
    print(f"Your score is {user_score}")
    result = get_result(user_score)
    print(result)
    """import a random number"""
    random_score = random.randint(0, 101)  #random.randint(low value, high value)
    print(f"Random score is {random_score}")
    result = get_result(random_score)
    print(result)


def get_result(score):
    """this function is to determine grade"""
    if score < MINIMUM_SCORE or MAXIMUM_SCORE > 100:
        message = "Invalid score"
    elif score >= EXCELLENT_THRESHOULD:
        message = "Excellent"
    elif score >= PASSABLE_THRESHOULD:
        message = "Passable"
    else:
        message = "Bad"

    return message


main()
