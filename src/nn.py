from layer import Layer
from matrix import Matrix


class NeuralNetwork:
    """A fully-connected neural network."""

    def __init__(self, structure):
        """Creates a neural network.

        Arguments:
            structure (array): Array of numbers giving the number of neurons in
            each layer of the neural network.
        """

        self.first_layer = Layer(structure[0])
        self.last_layer = self.first_layer
        self.loss = 0

        for i in range(1, len(structure)):
            self.last_layer = Layer(structure[i], self.last_layer)

    def feedforward(self, inputs):
        self.first_layer.load_data(inputs)
        return self.last_layer.compute()

    def train(self, inputs, targets, learning_rate=0.1):
        """Adjusts the weights and biases of the neural network.

        Arguments:
            inputs (array): Array of inputs that should get 'targets' as a result.
            targets (array): The expected result from the inputs.
            learning_rate (float): The learning rate for the step of the training.
        """

        self.first_layer.load_data(inputs)
        self.last_layer.compute()
        last_layer_error = self.last_layer.activations - Matrix([[e] for e in targets])
        self.last_layer.backpropagate(last_layer_error, learning_rate)

        loss = 0
        for i in range(last_layer_error.m):
            loss += last_layer_error[i, 0] ** 2

        loss /= last_layer_error.m
        self.loss = loss

