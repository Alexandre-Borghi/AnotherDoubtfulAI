from layer import Layer


class NeuralNetwork:
    """A fully-connected neural network."""

    def __init__(self, structure):
        """Creates a neural network.

        Arguments:
            structure (array): Array of numbers giving the number of neurons in
            each layer of the neural network.
        """

        self.layers = []

        self.layers.append(Layer(structure[0]))
        for i in range(1, len(structure)):
            self.layers.append(Layer(structure[i], self.layers[-1]))

    def feedforward(self, inputs):
        self.layers[0].load_data(inputs)
        return self.layers[-1].compute()

    def train(self, inputs, outputs):
        """Adjusts the weights and biases of this layer and backpropagates to
        previous layers.

        Arguments:
            inputs (array): Array of inputs that should get 'outputs' as a result.
            outputs (array): The expected result from the outputs.
        """

        pass
