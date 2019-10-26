from datetime import date
from gs_quant.data import Dataset
from gs_quant.markets.securities import SecurityMaster, AssetIdentifier
from gs_quant.session import GsSession

class Stock:
	def __init__(self):
		self.needs_name = True
		self.name = ""
		self.risk = []
		self.growth = []
		self.returns = []
		self.multiple = []
		self.factor = []

	def add_risk(self, risk_val):
		self.risk.append(risk_val)


	def rename(self, name):
		self.name = name
	def add_growth(self, growth_val):
		self.growth.append(growth_val)
	def add_returns(self, returns_val):
		self.returns.append(returns_val)
	def add_multiple(self, multiple_val):
		self.multiple.append(multiple_val)
	def add_factor(self, factor_val):
		self.factor.append(factor_val)
	def add_all(self, growth_val, returns_val, multiple_val, factor_val):
		add_growth(growth_val)
		add_returns(returns_val)
		add_multiple(multiple_val)
		add_factor(factor_val)		

yeet = open('C:/Users/User/Desktop/Hackathons/CalHacks6.0/CalHacks6.0MLPortfoli0-master/data_raw.txt', 'r')
identifiers = ["gsid", "assetId", "financialReturnsScore", "growthScore", "multipleScore", "integratedScore", "updateTime", "assetName", "date"]

stocks = []

current_line = (yeet.read().split())

cycle_count = 0
line_count = 0
stock_index = 0
stock_name = ""
for i in current_line:
	print(i)
	if i in identifiers:
		stock_name = ""
		cycle_count = 0
	else:
		if cycle_count % 9 == 0:
			if i == "2017-01-16":
				stocks.append(Stock())
				if len(stocks) > 1:
					stock_index += 1

		if cycle_count % 9 == 3:
			stocks[stock_index].add_returns(i)
		if cycle_count % 9 == 4:
			stocks[stock_index].add_growth(i)
		if cycle_count % 9 == 5:
			stocks[stock_index].add_multiple(i)	
		if cycle_count % 9 == 6:
			stocks[stock_index].add_factor(i)								
		if cycle_count % 9 == 8:
			if i[0:4] != "2017":
				stock_name += i + " "
				cycle_count -= 1
			else:
				cycle_count += 1
				if stocks[stock_index].needs_name == True:
					stocks[stock_index].rename(stock_name)
					stocks[stock_index].needs_name = False
		cycle_count += 1
		#sprint("cycle_count = "+ str(cycle_count))


print()
print()
print("Number of stocks: " + str(len(stocks)))
print()

for i in stocks:
	print(i.name)
	print("Growth")
	print(i.growth)
	print("Returns")
	print(i.returns)
	print("Multiple")
	print(i.multiple)
	print("Factor")
	print(i.factor)
	print("-----------------\n")
print(str(cycle_count))	
