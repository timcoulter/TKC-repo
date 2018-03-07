no_items = int(input("Enter number of items:"))
if no_items <= 0:
    print("You need a value larger than 0")
    no_items = int(input("Enter number of items:"))

prices = list()
counter = 1
for i in range(no_items):
    print("What is the price of item {0}".format(counter))
    price = float(input("$"))
    if price <= 0:
        print('Items are not free!')
        continue
    counter += 1
    prices.append(price)

total_payment=0
for amounts in prices:
    total_payment += amounts
if total_payment > 100:
    total_payment *= 0.9
print('The total price is:{0}'.format(total_payment))

