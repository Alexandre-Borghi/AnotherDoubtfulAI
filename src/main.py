from nn import NeuralNetwork

# AND example

nn = NeuralNetwork([2, 3, 1])

data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
]

targets = [
    [0],
    [0],
    [0],
    [1],
]

print(nn.feedforward(data[0]).activations.rows)
