from __future__ import absolute_import, division, print_function, unicode_literals
import statistics
import pathlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers

print(tf.__version__)
from src import data_refactoring


def get_stocks(stocks):
    stock_list = []
    price_list = []
    mean_list = []
    std_list = []
    for stock in stocks:
        growth = np.array(stock.growth)
        returns = np.array(stock.returns)
        multiple = np.array(stock.multiple)
        value = np.array(stock.value)
        matrix_of_stock = np.column_stack((growth, returns, multiple))
        mean_list.append(np.mean(growth))
        mean_list.append(np.mean(returns))
        mean_list.append(np.mean(multiple))
        mean_list.append(np.mean(value))
        std_list.append(np.stdev(growth))
        std_list.append(np.stdev(returns))
        std_list.append(np.stdev(multiple))
        std_list.append(np.stdev(value))
        stock_list.append(matrix_of_stock)
        price_list.append(value)
    return stock_list, price_list, mean_list, std_list

def normalize(growth, returns, multiple, value, mean, std):
    index = 0
    for i in range(mean):
        if index % 4 == 0:
            growth[(index / 4) % 1] = (growth[(index / 4) % 1] - mean[i])/std[i]
        if index % 4 == 1:
            returns[(index / 4) % 1] = (returns[(index / 4) % 1] - mean[i])/std[i]
        if index % 4 == 2:
            multiple[(index / 4) % 1] = (multiple[(index / 4) % 1] - mean[i])/std[i]
        if index % 4 == 3:
            value[(index / 4) % 1] = (value[(index / 4) % 1] - mean[i]) / std[i]
        index +=1
    return growth, returns, multiple, value

def regression(X , Y):

    X_total = pd.DataFrame({'growth': X[:, 0]}, {'returns': X[:, 1]}, {'multiple': X[:, 2]})
    Y_total = pd.DataFrame({'price': Y[:, 0]})
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=[len(X_total.keys())]),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['mae', 'mse'])
    model.summary()






