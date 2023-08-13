"""
Word Occurrences
Estimate: 60 minutes
Actual:   150 minutes
"""

import csv


def main():
    data = csv_reader()
    champions = get_champions(data)
    print("Wimbledon Champions:")
    for name, wins in champions.items():
        print(f"{name} {wins}")

    countries = get_countries(data)
    print("\nThese", len(countries), "countries have won Wimbledon:")
    countries_string = ", ".join(countries)
    print(countries_string)


def csv_reader():
    with open('wimbledon.txt', "r", encoding="utf-8-sig") as in_file:
        data = []
        csv_reader = csv.reader(in_file)
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
        return data


def get_champions(data):
    champions = {}
    for row in data:
        name = row[2]
        if name in champions:
            champions[name] += 1
        else:
            champions[name] = 1
    return champions


def get_countries(data):
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)


main()
