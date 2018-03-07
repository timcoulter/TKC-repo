
out_file = open('conrads_stock_price.txt', 'w')
INITIAL_PRICE = 10.0
MIN_PRICE = 0.01
MAX_PRICE = 100.0; MAX_INCREASE = 0.175; MAX_DECREASE = 0.05
price = list();counter = 0; price_change = 0; new_price=0
price.append(INITIAL_PRICE)
print("Staring Price:","${:,.2f}".format(INITIAL_PRICE))

while price[counter] >= MIN_PRICE and price[counter] <= MAX_PRICE:
 counter += 1
 if random.randint(1, 2) == 1:
  price_change = random.uniform(0, MAX_INCREASE)
 else:
  price_change = random.uniform(-MAX_DECREASE, 0)
 new_price = price[counter-1] + price_change
 price.append(new_price)
 print_format_loophole = round(price[counter],2)
 print("On day {0} the price is: ${1}".format(counter,print_format_loophole),file = out_file)

out_file.close()


