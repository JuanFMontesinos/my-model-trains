from typing import Union, List

import matplotlib.pyplot as plt
import numpy as np

from .regressor import *


def simple_plot(X: np.array, Y: np.array, title: str = None, xlabel: str = None, ylabel: str = None, **kwargs):
    plt.plot(X, Y, **kwargs)
    plt.grid(True)
    if title is not None:
        plt.title(title)
    if xlabel is not None:
        plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)


def plot_and_regress(X: np.array, Y: np.array,
                     title: str = None, xlabel: str = None, ylabel: str = None,
                     regressors: Union[List[str], None] = None,
                     verbose: bool = False,
                     n_values: int = None,
                     **kwargs) -> dict:
    """
    Adjust the data to a logarithmic function or power-law function and plot it.
    args:
        X: x-axis values (np.array) starting from 1. Usually np.arange(1, 1 + len(Y))
        Y: y-axis values (np.array)
        title: (optional) title of the plot
        xlabel: (optional) x-axis label
        ylabel: (optional) y-axis label
        regressors: (optional) list of regressors to use. If None, just plots the raw data.
        verbose: (optional) if True, prints the results of the regressions
        n_values: (optional) number of X points to plot the regressions. If None, plots all values.
        kwargs: (optional) arguments to pass to plt.plot()

    returns:
        results: dictionary with the results of the regressions.

    """
    assert len(X) == len(Y), "X and Y must have the same length"
    simple_plot(X, Y, title, xlabel, ylabel)
    if n_values is None:
        n_values = len(X)
    x_plot = np.arange(1, n_values)
    results = {}
    if regressors is not None:
        for regressor in regressors:
            if regressor == 'power_law':
                A, B = regress_power_law(X, Y)
                results['power_law'] = {'A': A, 'B': B, 'R2': abs_error(Y, power_law(X, A, B))}
                if verbose:
                    print(f'Power law: A = {A}, B = {B}, R^2 = {results["power_law"]["R2"]}')
                simple_plot(x_plot, power_law(x_plot, A, B), **kwargs.get(regressor, {}))
            elif regressor == 'natural_log':
                A, B = regress_natural_log(X, Y)
                results['natural_log'] = {'A': A, 'B': B, 'R2': abs_error(Y, natural_log(X, A, B))}
                if verbose:
                    print(f'Natural log: A = {A}, B = {B}, R^2 = {results["natural_log"]["R2"]}')
                simple_plot(x_plot, natural_log(x_plot, A, B), **kwargs.get(regressor, {}))
            else:
                raise ValueError(f'Unknown regressor: {regressor}')
        plt.legend(regressors)
    return results
