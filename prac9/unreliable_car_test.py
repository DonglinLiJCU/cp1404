import random

from unreliable_car import UnreliableCar

my_car = UnreliableCar("car", 100, 60)

rand_int = random.randint(0, 100)
print("randint: " + str(rand_int))
my_car.drive(rand_int)

print(my_car)
