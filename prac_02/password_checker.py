
MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    validity = False
    while validity == False:
        print("Please enter a valid password")
        print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
              "characters, and contain:")
        print("\t1 or more uppercase characters")
        print("\t1 or more lowercase characters")
        print("\t1 or more numbers")
        if SPECIAL_CHARS_REQUIRED:
            print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
        password = input("> ")
        validity = password_test(password)

        if validity == False:
            print("Invalid password!")
            message = 'invalid'
        else:
            message = 'valid'
        print("Your {0}-character password is {1}: {2}".format(len(password), message, password))

def password_test(password):
    count_lower, count_upper, count_digit, count_special = 0, 0, 0, 0
    key1, key2, key3, key4, key5 = "", "", "", "", ""
    length = len(password)
    validity = True
    if length not in range(2, 6):
        key1 = "The entered password is not the required length."
        validity = False
    else:
        for i in password:
            if i.islower():
                count_lower += 1
            if i.isupper():
                count_upper += 1
            if i.isdigit():
                count_digit += 1
            if i in SPECIAL_CHARACTERS:
                count_special += 1
        if count_lower == 0:
            validity = False
            key2 = "A lower case letter character must be entered."
        if count_upper == 0:
            validity = False
            key3 = "An upper case character must be entered."
        if count_digit == 0:
            validity = False
            key4 = "A number must be entered."
        if SPECIAL_CHARS_REQUIRED == True:
            if count_special == 0:
                validity = False
                key5 = "A special character must be entered."
    if validity != False:
        return validity
    else:
        print(key1, '\n', key2, '\n', key3, '\n', key4, '\n', key5, '\n', sep='')
        return validity
main()
