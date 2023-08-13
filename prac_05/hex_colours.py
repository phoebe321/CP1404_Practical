COLOUR_HEX = {"Black": '#000000', "Buff": '#f0dc82', "Camel": '#c19a6b', "Gray": '#bebebe',
                "Iceberg": '#71a6d2', "Opal": '	#a8c3bc', "Pale": '	#db7093', "Pear": '	#d1e231', "Puce": '	#cc8899', "Straw": '#e4d96f'}

colour_name = input("Enter colour name: ").title()
# print(COLOUR_HEX[colour_name])

while colour_name != "":
    try:
        print(COLOUR_HEX[colour_name])
    except KeyError:
        print("Invalid name")
    colour_name = input("Enter colour name: ").title()