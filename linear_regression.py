import tensorflow as tf
import numpy as np
import pandas as pd

epochs = 10
learning_rate = 0.2

x_train_numpy = np.zeros()
y_train_numpy = np.zeros()
x_test_numpy = np.zeros()
y_test_numpy = np.zeros()


price  = tf.placeholder(float)
dates = tf.placeholder(int)
W = tf.Variable(np.random.randn, name = "W")
b = tf.Variable(np.random.randn, name ="b")
X_train = tf.convert_to_tensor(x_train_numpy)
Y_train = tf.convert_to_tensor(y_train_numpy)
X_test = tf.convert_to_tensor(x_test_numpy)
Y_test = tf.convert_to_tensor(y_test_numpy)

moving_average = tf.train.ExponentialMovingAverage(decay = 0.999)

Y = tf.add(tf.mult(W, b), X_train)

loss_function = tf.reduce_mean(tf.squared_difference(Y, Y_test))
optimizer = tf.train.AdamOptimizer().minimize(loss_function)

with tf.Session as sess:
    for epoch in range(epochs):
        