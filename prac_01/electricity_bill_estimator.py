dollars_per_kwh = input("Enter dollars per kwh:")
use_per_day = input("Enter daily use in kwh:")
no_of_billing_days = input("Enter the number of billing days:")
TARIFF_11 = 0.244618
TARIFF_31 = 0.136980

tariff_message = input("Which tarrif are you using, 11 or 31:")
if tariff_message == 11:
    tariff = float(TARIFF_11)
else:
    tariff = float(TARIFF_31)

bill_without_tarrif = dollars_per_kwh*use_per_day*no_of_billing_days
total_bill = bill_without_tarrif + bill_without_tarrif*tariff

print("Your total bill is {0}".format(total_bill))
