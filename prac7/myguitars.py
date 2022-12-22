class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def __lt__(self, other):
        return self.get_age() > other.get_age()

    def get_age(self):
        return 2022 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False


def main():
    guitars = []
    in_file = open("guitars.csv", "r")
    for line in in_file:
        parts = line.strip().split(',')
        guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    guitars.sort()
    print("Initial guitars:")
    for guitar in guitars:
        print(guitar)

    print()
    print("Add new guitar:")
    while True:
        name = input("Name: ")
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        print(add_guitar(name, year, cost, guitars))
        print()

    print()
    print("... snip ...")
    print()
    print("These are my guitars:")
    write_to_csv(guitars)
    for i in out(guitars):
        print(i)


def add_guitar(name, year, cost, guitars):
    guitars.append(Guitar(name, year, cost))
    return f"{name} ({year}) : ${cost:.2f} added."


def out(guitars):
    output = []
    for index, item in enumerate(guitars):
        tmp = f"Guitar {index + 1}: {item.name:>40} ({item.year}), worth ${item.cost:10,.2f} (vintage)" if item.is_vintage() \
            else f"Guitar {index + 1}: {item.name:>40} ({item.year}), worth ${item.cost:10,.2f}"
        output.append(tmp)
    return output


def write_to_csv(guitars):
    in_file = open("guitars.csv", "w")
    for guitar in guitars:
        in_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    in_file.close()


main()
