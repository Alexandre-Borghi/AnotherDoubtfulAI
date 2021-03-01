from matrix import Matrix
from utils import leaky_relu, leaky_relu_prime


class Layer:
    """Represents a neural network's hidden layer."""

    def __init__(
        self,
        neurons,
        prev_layer=None,
        activation_func=leaky_relu,
        activation_func_deriv=leaky_relu_prime,
    ):
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
            self.activation_func_deriv = activation_func_deriv

    def get_neurons_count(self):
        """Returns the number of neurons in the layer."""

        return self.activations.m

    def is_input_layer(self):
        """Returns True if layer is an input layer."""

        return self.prev_layer is None

    def load_data(self, data):
        """Loads data from an array that should have the same number of elements
        than the number of neurons in the layer. Use this function to put data in
        in the input layer.

        Arguments:
            data (array): Array of numbers to put in the activations matrix.
        """

        self.activations = Matrix([[data[i]] for i in range(len(data))])

    def compute(self, modify=True):
        """Computes the new values from the previous layer and returns the new
        values of the neurons. Does nothing if layer is an input layer.

        Arguments:
            modify (boolean): Set to False if the activations of the layer should
            not be modified. Useful during backpropagation.
        """

        if self.is_input_layer():
            return self.activations

        new_activations = (
            self.weights.get_transpose() * self.prev_layer.compute(modify) + self.biases
        ).map(self.activation_func)

        if modify:
            self.activations = new_activations

        return new_activations

    def backpropagate(self, error, learning_rate=0.1):
        """Changes the weights and biases of this layer and backpropagates to
        previous layer.
        Should only be used externally on the last layer of the neural network.

        Arguments:
            error (Matrix): Column matrix of the difference between the results
            (activations) of this layer and the expected results.
        """

        # Resource used for the equations : https://sudeepraja.github.io/Neural/

        if self.is_input_layer():
            return

        activations_deriv = (
            (self.weights.get_transpose() * self.prev_layer.activations)
            .copy()
            .map(self.activation_func_deriv)
        )
        d = error.el_wise_mul(activations_deriv) * learning_rate
        delta_weights = d * self.prev_layer.activations.get_transpose()
        delta_weights.transpose()

        self.weights -= delta_weights
        self.biases -= d

        next_error = self.weights * error

        self.prev_layer.backpropagate(next_error, learning_rate)
