from math import exp


def is_a_number(number):
    return type(number) in (int, float, complex)


def sigmoid(x):
    return 1 / (1 + exp(-x))


def d_sigmoid(x):
    """The derivative of the sigmoid function."""

    return sigmoid(x) * (1 - sigmoid(x))
