from matrix import Matrix
from utils import sigmoid


class Layer:
    """Represents a neural network's hidden layer."""

    def __init__(self, neurons, prev_layer=None, activation_func=sigmoid):
        """Creates a neural network layer.
        
        Arguments:
            neurons (int): The number of neurons in the layer.
            prev_layer (Layer): The previous layer. Leave None if input layer.
            activation_func (Function): The activation function used in this layer.
        """

        self.prev_layer = prev_layer
        self.activations = Matrix.zeros((neurons, 1))

        if not self.is_input_layer():
            self.weights = Matrix.random((self.prev_layer.get_neurons_count(), neurons))
            self.biases = Matrix.random((neurons, 1))
            self.activation_func = activation_func

    def get_neurons_count(self):
        """Returns the number of neurons in the layer."""

        return self.activations.m

    def is_input_layer(self):
        """Returns True if layer is an input layer."""

        return self.prev_layer is None

    def compute(self):
        """Computes the new values from the previous layer and returns self.
        Does nothing if layer is an input layer.
        """

        if self.is_input_layer():
            return self

        self.activations = (
            self.weights.get_transpose() * self.prev_layer.compute().activations
            + self.biases
        ).map(self.activation_func)

        return self

    def load_data(self, data):
        """Loads data from an array that should have the same number of elements
        than the number of neurons in the layer. Use this function to put data in
        in the input layer.

        Arguments:
            data (array): Array of numbers to put in the activations matrix.
        """

        self.activations = Matrix([[data[i]] for i in range(len(data))])
