from matrix import Matrix

class Layer:
    """Represents a neural network's hidden layer."""

    def __init__(self, neurons, prev_layer=None):
        """Creates a neural network layer.
        
        Arguments:
            neurons (int): The number of neurons in the layer.
            prev_layer (Layer): The previous layer. Leave None if input layer.
        """

        self.prev_layer = prev_layer
        self.activations = Matrix((neurons, 1))

        if self.prev_layer is not None:
            self.weights = Matrix.random(
                (neurons, self.prev_layer.get_neurons_count())
            )
    
    def get_neurons_count(self):
        return self.activations.m
