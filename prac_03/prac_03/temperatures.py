def main ():
    conversion = input('Convert from celsius or farenheit: ').strip().lower()
    while conversion.isdigit:
        conversion = input('Convert from celsius or fahrenheit: ').strip()
    value = input('Enter temperature value: ').strip()
    while value.isalpha:
        value = input('Enter a number for a value: ')
    if conversion == 'celsius':
        celsius_to_fahrenheit(int(value))
    elif conversion == 'fahrenheit':
        fahrenheit_to_celsius(int(value))

def celsius_to_fahrenheit(value):
    result = (value)*(9 / 5) + 32
    print('{0} degrees celsius is equal to {1} degrees fahrenheit'.format(value, result))

def fahrenheit_to_celsius(value):
    result = (value)*(5 / 9) - 32
    print('{0} degrees fahrenheit is equal to {1} degrees celsius'.format(value, result))

main()





