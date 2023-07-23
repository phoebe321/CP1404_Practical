MINIMUM_PASSWORD_LENGTH = 5


def main():
    """display output"""
    password = get_password()
    display_asterisks(password)


def get_password():
    """get user input & do the checking"""
    password = input("Enter a password (minimum {} characters): ".format(MINIMUM_PASSWORD_LENGTH))
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print("Password must be at least {} characters long. Try again.".format(MINIMUM_PASSWORD_LENGTH))
        password = input("Enter a password (minimum {} characters): ".format(MINIMUM_PASSWORD_LENGTH))

    return password


def display_asterisks(password):
    """display the asterisks according to the length of the password"""
    print("*" * len(password))


main()

