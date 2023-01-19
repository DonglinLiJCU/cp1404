from car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance if distance < self.reliability else 0)
        self.current_fare_distance += distance_driven
        return distance_driven
