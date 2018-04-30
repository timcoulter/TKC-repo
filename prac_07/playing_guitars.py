from Guitars import Guitar
guitars = [Guitar('Fender Stratocaster', 2014, 765.4), Guitar("Gibson L-5 CES", 1922, 16035.40),
           Guitar('Line 6 JTV-59', 2010, 1512.9)]

def get_guitars():
    guitars = list()
    user_input = input('Add a guitar? (y/n)\n>>>')
    if user_input == 'y':
        new_name = input('Enter name of guitar: ')
        while len(new_name) == 0:
            new_name = input('Name cannot be blank!\nEnter name of guitar: ')
        new_year = add_number('integer', 'Enter year guitar was made: ')
        new_price = add_number('float', 'Enter price of guitar: ')
        guitars.append(Guitar(new_name, new_year, new_price))
    elif len(guitars) == 0:
        print('You have no guitars')






def add_number(message, numtype='float'):
    try:
        if numtype == 'integer':
            user_input = int(input(message))
        else:
            user_input = float(input(message))
    except ValueError:
        print('Number must be a {0}'.format(numtype))
        add_number(numtype, message)
    else:
        return user_input

def display_guitars(guitars):
    if len(guitars) == 0:
        print('You have no guitars :(')
    else:
        longest_guitar_name = max([len(guitar.name) for guitar in guitars])
        longest_guitar_price = max([len(str(guitar.cost)) for guitar in guitars])
        print('These are my guitars:')
        for i, guitar in enumerate(guitars, 1):
            if guitar.is_vintage():
                vintage = '(vintage)'
            else:
                vintage = ''
            print('Guitar {0}: {1}{2} ({3}), worth ${4}{5} {6}'.format(i, (longest_guitar_name - len(guitar.name))*' ',
                                                                       guitar.name, guitar.year,
                                                                       (longest_guitar_price - len(str(guitar.cost)))*' ',
                                                                        guitar.cost, vintage))



display_guitars(guitars)