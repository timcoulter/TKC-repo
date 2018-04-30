from random import randint
from cars import Car

class Unreliable_car(Car):
    """An unreliable version of a car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car, only sometimes, based on reliability."""
        random_number = randint(1, 100)
        distance_driven = 0
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            print('You are out of luck today, car wont drive :(')
        return distance_driven


dodgy_car = Unreliable_car('Ford ute', 120, 40)
dodgy_car.drive(40)
print(dodgy_car)
