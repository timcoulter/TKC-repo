from test_taxi import Taxi
from cars import Car

class SilverServiceTaxi(Taxi):

    def __init__(self, name, fuel, fanciness=1, flagfall=4.50):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.flagfall = flagfall

    def __str__(self):
        return str('{0} plus flagfall of ${1}'.format(super().__str__(), self.flagfall))

    def get_fare(self):
        return super().get_fare()*self.fanciness + self.flagfall

def main():
    fancy_taxi = SilverServiceTaxi('Hummer', 200, 2)
    print(fancy_taxi)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print('The fare is currently ${0}'.format(fancy_taxi.get_fare()))
#main()
