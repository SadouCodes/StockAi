import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np

# uses numpy to create arrays and store data
# x is the input data
# y is the output data
x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([[0], [1], [1], [0]])


# Define network model and its arguments
# Define number of nodes and neurons in each layer

model = Sequential()
# Creates a model object, arranges layers in sequence

model.add(Dense(2, input_shape=(2,)))  
# 2 neurons in the first hidden layer, input_shape = (2,) means 2 neurons in the input layer

model.add(Activation('sigmoid')) 
# activation function for hidden layer

model.add(Dense(1)) 
# output layer, 1 neuron 

model.add(Activation('sigmoid'))
# activation function for output layer

model.compile(optimizer='sgd', loss='mean_squared_error', metrics=['accuracy'])
# optimizer = 'sgd' means stochastic gradient descent
# loss = 'mean_squared_error' means mean squared error
# metrics = ['accuracy'] means it tests accuracy

# Compiles the method and calculates it accuracy

model.summary()
# Prints a summary of the model