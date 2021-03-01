from nn import NeuralNetwork
from random import randint, seed

# XOR example

nn = NeuralNetwork([2, 4, 1])

data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
]

targets = [
    [0],
    [1],
    [1],
    [0],
]


for _ in range(10000):
    i = randint(0, len(data) - 1)
    nn.train(data[i], targets[i], 0.1)


print(nn.feedforward(data[0]).rows)
print(nn.feedforward(data[1]).rows)
print(nn.feedforward(data[2]).rows)
print(nn.feedforward(data[3]).rows)
print("----")

# NOT example

nn = NeuralNetwork([1, 1, 1])

data = [[0], [1]]
targets = [[1], [0]]

for _ in range(0):
    i = randint(0, len(data) - 1)
    nn.train(data[i], targets[i], 0.1)

print(nn.feedforward(data[0]).rows)
print(nn.feedforward(data[1]).rows)
