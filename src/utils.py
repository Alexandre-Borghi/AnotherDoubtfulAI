from math import exp


def is_a_number(number):
    return type(number) in (int, float, complex)


def sigmoid(x):
    return 1 / (1 + exp(-x))


def sigmoid_prime(x):
    """The derivative of the sigmoid function."""

    return sigmoid(x) * (1 - sigmoid(x))


def relu(x):
    return max(0, x)


def relu_prime(x):
    return 0 if x < 0 else 1


def leaky_relu(x):
    return max(0.01 * x, x)


def leaky_relu_prime(x):
    return 0.01 if x < 0 else 1


def from_rgb(r, g, b):
    """Translates an rgb color of 0.0-1.0 floats to a tkinter friendly color code
    """

    r, g, b = int(r * 255), int(g * 255), int(b * 255)

    return "#%02x%02x%02x" % (r, g, b)
