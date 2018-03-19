"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""

def main():
    """Requests for user input for income per month, for a given number of months.
    The data is then appended to a list"""
    incomes = []
    total_months = int(input("How many months? "))

    for month in range(1, total_months + 1):
        income = float(input("Enter the income for the month {0}:".format(month)))
        incomes.append(income)
    print_report(total_months, incomes)

def print_report(total_months, incomes):
    """Print income report for given incomes over a given number of months"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, total_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()