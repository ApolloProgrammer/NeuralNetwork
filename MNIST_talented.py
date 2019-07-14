import NeuralNetwork as NN
import csv
import numpy
from numpy import genfromtxt
import pandas as pd

#reading in the data
wih = genfromtxt('data/wih.csv', delimiter=',')
who = genfromtxt('data/who.csv', delimiter=',')
bih = genfromtxt('data/bih.csv', delimiter=',')

bih_data=[]
for element in bih:
    bih_data.append([element])
    bih=numpy.array(bih_data)
bho = genfromtxt('data/bho.csv', delimiter=',')
bho_data=[]
for element in bho:
    bho_data.append([element])
    bho=numpy.array(bho_data)

# print('wih')
# print(len(wih))
# print('who')
# print(who)
# print('bias_ih')
# print(bih)
# print('bias_h0')
# print(bho)
# print('FINISH1')

#number of input, hidden and output nodes, learning rate
input_nodes = 784
hidden_nodes = 200
output_nodes = 10
learning_rate = 0.1
# create instance of neural network
brain = NN.NeuralNet(input_nodes,hidden_nodes,output_nodes, learning_rate)

brain.wih=wih
brain.who=who
brain.bias_ih=bih
brain.bias_ho=bho

# load the mnist test data CSV file into a list
test_data_file = open("mnist_dataset/mnist_test.csv", 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# test the neural network

# scorecard for how well the network performs, initially empty
scorecard = []

# go through all the records in the test data set
for record in test_data_list:
    # split the record by the ',' commas
    all_values = record.split(',')
    # correct answer is first value
    correct_label = int(all_values[0])
    # scale and shift the inputs
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    # query the network
    outputs = brain.query(inputs)
    # the index of the highest value corresponds to the label
    label = numpy.argmax(outputs)
    # append correct or incorrect to list
    if label == correct_label:
        # network's answer matches correct answer, add 1 to scorecard
        scorecard.append(1)
    else:
        # network's answer doesn't match correct answer, add 0 to scorecard
        scorecard.append(0)
        pass
    pass

# calculate the performance score, the fraction of correct answers
scorecard_array = numpy.asarray(scorecard)
print("performance = "+str(scorecard_array.sum() / scorecard_array.size))