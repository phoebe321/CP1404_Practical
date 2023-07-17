"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

"""
score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    elif score > 50:
        print("Passable")
    else:
        print("Excellent")
if score < 50:
    print("Bad")
"""

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOULD = 90
PASSABLE_THRESHOULD = 50

score = float(input("Enter score: "))
if score < MINIMUM_SCORE or MAXIMUM_SCORE > 100:
    message = "Invalid score"
elif score >= EXCELLENT_THRESHOULD:
    message = "Excellent"
elif score >= PASSABLE_THRESHOULD:
    message = "Passable"
else:
    message = "Bad"

print(message)

