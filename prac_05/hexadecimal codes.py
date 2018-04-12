
def main():
    with open('hexadecimal codes.txt','r') as hexfile:
        lines = hexfile.readlines()
    hexkey = list()
    hexval = list()
    for line in lines:
        line = line.replace('\t','')
        hashspot = line.find('#')
        hexkey.append(line[0:hashspot-1])
        hexval.append(line[hashspot:-1])
    hexdict = dict(zip(hexkey, hexval))
    print(hexdict)
    menu(hexdict)

def menu(hexdict):

    user_input = input('Search for a colour code? (y/n)\n>>>')
    if user_input == 'y':
        colour_search(hexdict)
        menu(hexdict)
    elif user_input == 'n':
        print('Goodbye')
    else:
        print('Please enter y or n to choose.')
        menu(hexdict)

def colour_search(hexdict):
    try:
        user_input = input('Enter colour name: ')
        print(hexdict.get(user_input))
    except KeyError:
        print('The colour you entered is not a hexidecimal colour')
        colour_search(hexdict)
    with open('searched colours.txt', 'a+') as file:
        output_string = user_input + '\t' + hexdict.get(user_input) + '\n'
        file.write(output_string)

main()

