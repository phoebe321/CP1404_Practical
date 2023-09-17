

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    bill_to_date = 0

    MENU = "q)uit, c)hoose taxi, d)rive"
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)
            taxi_choice = input("Choose taxis: ")
            try:
                taxi_choice = int(taxi_choice)
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                    print(f"Bill to date: ${bill_to_date:.2f}")
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input")

        elif choice == "d":
            if current_taxi is not None:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()
                    fare = current_taxi.drive(distance)
                    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                    bill_to_date += fare
                    print(f"Bill to date: ${bill_to_date:.2f}")
                except ValueError:
                    print("Invalid input")
            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display the available taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i}- {taxi}")


main()
