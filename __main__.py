from src import data_refactoring
from src import linear_regression
import numpy as np


stocks = data_refactoring.createStockList()
stocks, values, means, stds= linear_regression.get_stocks(stocks)
linear_regression.regression(stocks[0], values[0], means, stds)
