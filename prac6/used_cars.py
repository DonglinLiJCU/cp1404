"""
CP1404 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

"""
used_cars
Estimate: 2 minutes
Actual:   1 minutes
"""

from prac6.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Benz", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)


main()
