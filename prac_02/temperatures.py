
def main():
    """get user input"""
    choice = input("Enter choice (C or F): ").lower()
    if choice == "c":
        celsius = int(input("celsius: "))
        fahrenheit = get_celsius(celsius)
        print(fahrenheit)
    elif choice == "f":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = get_fahrenheit(fahrenheit)
        print(celsius)


def get_celsius(celsius):
    """celsius to fahrenheit"""
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


def get_fahrenheit(fahrenheit):
    """fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()

