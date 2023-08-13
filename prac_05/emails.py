"""
Word Occurrences
Estimate: 45 minutes
Actual:   60 minutes
"""


emails = {}

while True:
    email = input("Email: ")
    if not email:
        break

    email_parts = email.split("@")
    name_parts = email_parts[0].split(".")
    name = " ".join(name_parts)
    name.title()

    choice = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if choice == '' or choice == 'y':
        emails[name] = email
    else:
        names = input("Name: ").title()
        emails[names] = email

for name, email in emails.items():
    print(f"{name} ({email})")




