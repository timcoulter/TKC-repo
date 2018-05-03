class Guitar:
    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return '{0} ({1}) : ${2}'.format(self.name, self.year, self.cost)

    def get_age(self):
        return 2018 - self.year

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        return False

def main():
    guitar1 = Guitar('Gibson L-5', 1923, 16035)
    print(guitar1)
    print(guitar1.is_vintage(),'\n')
    guitar2 = Guitar('Another Guitar', 2013, 2000)
    print(guitar2)
    print(guitar2.is_vintage())
main()
