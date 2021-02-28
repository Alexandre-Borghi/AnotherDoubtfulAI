from layer import Layer

# XOR example

inputs = Layer(2)
output = Layer(1, inputs)

data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1],
]

inputs.load_data(data[0])
output.compute()

print(output.activations.rows)
