"""

get name
display menu
get choice
while choice != Q
   if choice == H
      display hello
   else if choice == G
      display goodbye
   else
      display invalid choice
   display menu
   get choice
display finished
"""

name = input("Enter name: ")
print("(H)ello", "\n(G)oodbye", "\n(Q)uit")
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid message")
    print("(H)ello", "\n(G)oodbye", "\n(Q)uit")
    choice = input(">>> ").upper()
print("Finished message")

