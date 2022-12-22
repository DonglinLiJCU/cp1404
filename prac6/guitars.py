"""
Guitars
Estimate: 5 minutes
Actual:   4 minutes
"""

from prac6.guitar import Guitar

guitars = []

guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))


def main():
    print("My guitars!")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(add_guitar(name, year, cost))
        print()

    print()
    print("... snip ...")
    print()
    print("These are my guitars:")
    for i in out():
        print(i)

def add_guitar(name, year, cost):
    guitars.append(Guitar(name, year, cost))
    return f"{name} ({year}) : ${cost:.2f} added."


def out():
    output = []
    for index, item in enumerate(guitars):
        tmp = f"Guitar {index + 1}: {item.name:>20} ({item.year}), worth ${item.cost:10,.2f} (vintage)" if item.is_vintage() \
            else f"Guitar {index + 1}: {item.name:>20} ({item.year}), worth ${item.cost:10,.2f}"
        output.append(tmp)
    return output


main()