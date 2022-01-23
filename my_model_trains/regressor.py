from typing import Tuple
import numpy as np


# Functionals
def power_law(x, A, B):
    return A * x ** B


def natural_log(x, A, B):
    return A * np.log(x) + B


# Regressors

def regress_natural_log(x: np.array, y: np.array) -> Tuple[float, float]:
    """
        Natural log regression using least squares method
        Natural log formula: y = A * log(x) + B

    """
    assert len(x) == len(y)
    n = len(x)
    num = n * np.sum(y * np.log(x)) - np.sum(y) * np.sum(np.log(x))
    den = n * np.sum(np.log(x) ** 2) - np.sum(np.log(x)) ** 2
    A = num / den

    B = (np.sum(y) - A * np.sum(np.log(x))) / n
    return A, B


def regress_power_law(x: np.array, y: np.array) -> Tuple[float, float]:
    """
        Power-law regression using least squares method
        Power-law formula: y = A * x ** B
        args:
            x: x-axis data
        return:
            A, B
    """
    assert len(x) == len(y)
    n = len(x)
    num = n * np.sum(np.log(x) * np.log(y)) - np.sum(np.log(x)) * np.sum(np.log(y))
    den = n * np.sum(np.log(x) ** 2) - np.sum(np.log(x)) ** 2
    B = num / den
    A = (np.sum(np.log(y)) - B * np.sum(np.log(x))) / n
    return np.exp(A), B


# Error functions

def rel_error(y: np.array, y_hat: np.array) -> float:
    """
        Relative error
        args:
            y: true value
            y_hat: predicted value
        return:
            relative error
    """
    return 100 * (np.linalg.norm(y - y_hat) / np.linalg.norm(y))


def abs_error(y: np.array, y_hat: np.array) -> float:
    """
        Absolute error
        args:
            y: true value
            y_hat: predicted value
        return:
            absolute error
    """
    return np.linalg.norm(y - y_hat)
