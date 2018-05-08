"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
        do_something(n - 1)
    elif n == 0:
        return
#do_something(4)

def blocks_for_n_rows(n):
    if n <= 0:
        return 0
    return n + blocks_for_n_rows(n-1)
#print(blocks_for_n_rows(6))