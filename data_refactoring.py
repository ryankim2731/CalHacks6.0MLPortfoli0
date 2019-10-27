from datetime import date
from gs_quant.data import Dataset
from gs_quant.markets.securities import SecurityMaster, AssetIdentifier
from gs_quant.session import GsSession
import numpy as np

class Stock:
	def __init__(self):
		self.needs_name = True
		self.name = ""
		self.symbol = ""
		self.risk = []
		self.growth = []
		self.returns = []
		self.multiple = []
		self.factor = []
		self.value = []

	def add_risk(self, risk_val):
		self.risk.append(risk_val)


	def add_value(self, value):
		self.value.append(value)
	def set_sybol(self, symbol):
		self.symbol = symbol
	def add_price(self, price):
		self.price.append(np.float32(price))
	def rename(self, name):
		self.name = name
	def add_growth(self, growth_val):
		self.growth.append(np.float32(growth_val))
	def add_returns(self, returns_val):
		self.returns.append(np.float32(returns_val))
	def add_multiple(self, multiple_val):
		self.multiple.append(np.float32(multiple_val))
	def add_factor(self, factor_val):
		self.factor.append(np.float32(factor_val))
	def add_all(self, growth_val, returns_val, multiple_val, factor_val):
		self.add_growth(growth_val)
		self.add_returns(returns_val)
		self.add_multiple(multiple_val)
		self.add_factor(factor_val)
def createStockList():
	yeet = open('C:/Users/ryank/Desktop/summercoding/CalHacks/src/data_raw.txt', 'r')
	identifiers = ["gsid", "assetId", "financialReturnsScore", "growthScore", "multipleScore", "integratedScore", "updateTime", "assetName", "date", "close", "volume"]

	stocks = []

	split_input = (yeet.read().split())

	cycle_count = 0
	line_count = 0
	stock_index = 0
	stock_name = ""
	for i in split_input:
		#print(i)
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
				try:
					stocks[stock_index].add_growth(i)
				except:
					pass
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

	yonk = open('C:/Users/ryank/Desktop/summercoding/CalHacks/src/hist_data_raw.txt', 'r')

	split_input = yonk.read().split()

	stock_index = -1
	cycle_count = 0
	for i in split_input:
		if i in identifiers:
			cycle_count = 0
			pass
		elif i[0:4] == "tick":
			cycle_count = 0
			pass
		else:
			if i == "2017-01-17":
				stock_index += 1
			if cycle_count % 3 == 2 and len(stocks[stock_index].value) < 120:
				(stocks[stock_index]).add_value(i)
		cycle_count += 1

	for i in stocks:
		if (len(i.multiple) != 120):
			i.multiple = i.multiple[0:120]

		if (len(i.returns) != 120):
			i.returns = i.returns[0:120]
	return stocks
