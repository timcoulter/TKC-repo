
def main():
    "This program stores 5 user input numbers and displays the first, last, smallest, largest and average number."
    numbers = list()
    for num in range(1,6):
        new_number = value_test()
        numbers.append(new_number)
    metadata(numbers)

def value_test():
    try:
        new_number = float(input("Number: "))
    except:
        new_number = float(input("A numerical value must be entered: "))
    return new_number

def metadata(numbers):
    first_number = numbers[0]
    last_number = numbers[-1]
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average_number = sum(numbers)/len(numbers)
    print("The first number is {0}\nThe last number is {1}\nThe smallest number is {2}\n"
          "The largest number is {3}\nThe average number is {4}".format(first_number,
            last_number, smallest_number, largest_number, average_number))


main()