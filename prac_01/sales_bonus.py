"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
#
# sales = float(input("Enter sales: $"))
# while sales >= 0:
#     if sales >= 1000:
#         bonus = sales * 0.15
#     else:
#         bonus = sales * 0.1
#
#     print(f"Bonus: ${bonus:.2f}")
#     sales = float(input("Enter sales: $"))


MINIMUM_SALE = 0
MAXIMUM_SALE = 1000
MINIMUM_DISCOUNT = 0.1
MAXIMUM_DISCOUNT = 0.5

sales = float(input("Enter sales: $"))
while sales >= MAXIMUM_SALE:
    if sales >= MAXIMUM_SALE:
        bonus = sales * MAXIMUM_DISCOUNT
    else:
        bonus = sales * MINIMUM_DISCOUNT

    print(f"Bonus: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))

