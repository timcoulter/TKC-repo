from cars import Car

class Taxi(Car):

    def __init__(self, name, fuel):
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.price_per_km = 1.23

    def __str__(self):
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

    def get_fare(self):
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        self.current_fare_distance = 0
        print('fare reset.')

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


def main():
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    print(my_taxi)
    print('Current fare is ${0}0.'.format(my_taxi.get_fare()))
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print('Current fare is ${0}0.'.format(my_taxi.get_fare()))

#main()