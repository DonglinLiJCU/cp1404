"""CP1404 Practical - Car class example."""
"""
Car class
Estimate: 5 minutes
Actual:   7 minutes
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name, fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance


def main():
    limo = Car("Benz", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)


if __name__ == '__main__':
    main()
