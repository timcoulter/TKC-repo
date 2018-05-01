
class Car:
    """Represent a Car object."""

    def __init__(self, name='',fuel=0):
        self.fuel = fuel
        self.odometer = 0
        self.name = name

    def __str__(self):
        return str('{}, fuel={}, odometer={}'.format(self.name, self.fuel, self.odometer))

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
        self.odometer += distance
        return distance

class Limo:
    """Represent a limo object."""

    def __init__(self, fuel=100):
        self.name = 'Limo'
        self.fuel = fuel
        self.odometer = 0

    def __add__ (self, more_fuel=20):
        self.fuel += more_fuel
        print(self.fuel)

    def __str__(self):
        return str('{}, fuel={}, {}'.format(self.name, self.fuel, self.odometer))

    def drive(self, distance=0):
        if distance >= self.fuel:
            print('Cannot drive that distance,\n{} will run out of fuel!!!'.format(self.id))
        else:
            self.odometer += distance
            self.fuel -= distance
            print('{}, fuel={}, {}'.format(self.name, self.fuel, self.odometer))


def main():
    """Demo test code to show how to use car class."""
    my_car = Car('Subaru',180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)



#main()