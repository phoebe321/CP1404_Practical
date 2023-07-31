
name = input("Name: ")
out_file = open("name.txt", "a")
print(name, file=out_file)
out_file.close()


try:
    filename = input("Enter filename: ")
    in_file = open(filename)
    text = in_file.read()
    in_file.close()
    print(f"Your name is {text}")

except FileNotFoundError:
    print("File not found")



with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()[:2]]
    result = sum(numbers)
    print("Result:", result)



try:
    with open("numbers.txt", "r") as file:
        all_numbers = []

        for line in file:
            numbers_in_line = line.strip().split()
            numbers_in_line = [int(num) for num in numbers_in_line]
            all_numbers.extend(numbers_in_line)

        if all_numbers:
            total = sum(all_numbers)
            print("Total:", total)
        else:
            print("The file is empty or contains no valid numbers.")
except FileNotFoundError:
    print("File 'numbers.txt' not found.")
except ValueError:
    print("Error: Invalid number format in the file.")
except Exception as error:
    print("An error occurred:", str(error))
