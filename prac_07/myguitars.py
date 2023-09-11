

from prac_06.guitar import Guitar


def main():
    """Read file of guitar details, save as objects, display."""
    guitars = []

    # Open the file for reading
    in_file = open('guitars.csv', 'r')
    in_file.readline()  # Consume the header line

    for line in in_file:
        parts = line.strip().split(',')
        language = Guitar(parts[0], parts[1], float(parts[2]))
        guitars.append(language)

    in_file.close()

    # Sort guitars based on year
    sorted_guitars = sorted(guitars, key=lambda x: x.year)

    # Print sorted guitar details
    for guitar in sorted_guitars:
        print(guitar)

# Call the main function
main()


