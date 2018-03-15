def main():
    result = []
    frequency = int(input('How many characters would you like to skip per letter in your name: '))
    name = get_name()
    for char in range(len(name)):
        if char % (frequency + 1) == 0:
            result.append(name[char])
    for letters in result:
        print(letters,end='')

def get_name():
    name = input('Enter your name here: ')
    name = name.strip()
    while not name.isalpha():
        print('A name is not a number')
        name = input('Enter your name here: ')
    return name

main()
