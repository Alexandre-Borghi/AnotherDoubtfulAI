from math import exp


def is_a_number(number):
    return type(number) in (int, float, complex)


def sigmoid(x):
    return 1 / (1 + exp(-x))
