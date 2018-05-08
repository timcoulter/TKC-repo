"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from cars import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    if n == 1:
        return n*s
    else:
        output = n * (' ' + s)
    return output[1:]


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly

    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    repeat_string("hi", 2)
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    test_car = Car()
    assert test_car.fuel == 0

run_tests()

def format_sentence(sentence=""):
    if len(sentence) == 0:
        return
    if not sentence[0].isupper():
        sentence = sentence[0].upper() + sentence[1:]
    if sentence[-1] != '.':
        sentence += '.'
    print(sentence)
    return sentence

assert format_sentence('hello') == 'Hello.'
assert format_sentence('my name is Tim') == 'My name is Tim.'


