
# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()

# for i in range(20,0,-1):
#     print(i, end=' ')
# print()

stars = int(input("Number of stars: "))
for i in range (stars + 1):
    print("*", end='')
print()



n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print('*' * i)
print()
