ss=str(input('The trading symbol is').replace('\n',''))
print('The trading symbol for the company is: ', ss)

principal1, price1=5000, 1.13
money1 = principal1*price1
print('Price of shares purvhased on Dec 1 2018: {} dollars'.format(money1))

principal2, price2=3567, 1.59
money2 = principal2*price2
print('Value of shares sold on Jan 1 2019: {} dollars.'.format(money2))
print('The amount of profit made on Jan 1: {} dollars.'.format(principal2*(price2-price1)))

principal3, price3=5000-3567, 1.8
money3 = principal3*price3
print('Value of shares sold on Jan 21: {} dollars.'.format(money3))
print('Profit for Jan 21 trade is: {} dollars.'.format(principal3*(price3-price1)))
p = money1 - (principal2*(price2-price1) + principal3*(price3-price1))
print('Total profit by trading the stock was: {} dollars.'.format(p))
