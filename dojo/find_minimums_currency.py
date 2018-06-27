currencies = [['dollars',100],['half_dollar',50], ['quarter',25],['dime',10], ['nickel', 5],['penny',1]]

def change(cents):
	coint = {}
	for currency in currencies:
		if cents % currency[1] == 0:
			coint[currency[0]] = cents // currency[1]
			break
		else:
			coint[currency[0]] = cents // currency[1]
			cents = cents % currency[1]
	return coint


result = change(314)
print(result)





