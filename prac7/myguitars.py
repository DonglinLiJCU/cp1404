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
    for guitar in guitars:
        print(guitar)


main()
