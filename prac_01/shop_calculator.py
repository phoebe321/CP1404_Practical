
# total = 0
# get number of count
# for i in range(1, number of count + 1)
#     number = float(input(f"Enter number {i}:"))
#     total = number + total
# display number of count & total


total = 0
DISCOUNT_THRESHOULD = 100
DISCOUNT_VALUE = 0.9

items = int(input("Number of count: "))

while items < 0:
    print("Invalid number of items!")
    items = int(input("Number of count: "))

for i in range(1, items + 1):
    price = float(input(f"Price of item {i}: "))
    total += price
    if total >= DISCOUNT_THRESHOULD:
        total *= DISCOUNT_VALUE

print(f"Total price for {items} items is ${total:.2f}")

