from test_taxi import Taxi
from silverservicetaxi1 import SilverServiceTaxi

def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = ''
    bill = 0.00
    user_input = input('q)uit, c)hoose taxi, d)rive\n>>> ').strip().lower()
    while user_input != 'q':
        if user_input == 'c':
            for i, taxi in enumerate(taxis):
                print('{0} - {1}'.format(i, str(taxi)))
            current_taxi = get_taxi(taxis, bill)
        elif user_input == 'd':
            if current_taxi == '':
                print('A taxi must be selected before driving!')

            else:
                taxis[current_taxi].drive(get_drive_distance(current_taxi, taxis))
                bill += taxis[current_taxi].get_fare()
                print('Your {0} trip cost you ${1}\nBill to date: ${2}'.format(taxis[current_taxi].name,
                      taxis[current_taxi].get_fare(), bill))
        elif user_input != 'c' or 'd' or 'q':
            print('Enter a valid choice')
        user_input = input('q)uit, c)hoose taxi, d)rive\n>>> ').strip().lower()










def get_taxi(taxis, bill):
    try:
        user_input = int(input('Choose taxi: '))
        if user_input not in range(0, len(taxis)-1):
            raise ValueError
    except ValueError:
        print('A valid taxi number must be selected!')
        get_taxi(taxis)
    print('Bill to date: $'.format(bill))
    return user_input

def get_drive_distance(current_taxi, taxis):
    try:
        user_input = int(input('Drive how far? '))
    except ValueError:
        print('Enter a valid integer distance')
        get_drive_distance(current_taxi, taxis)
    return user_input







main()