import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def create_normal_distribution(mu,
                               sigma,
                               min_value,
                               max_value,
                               size,
                               as_int=False,
                               plot_bins=None):
    
    """
    Creates normal distribution of randomly generated values with specified parameters.
    
    Parameters:
        mu (float or int): mean value for distribution
        sigma (float or int): standard deviation for distribution
        min_value (float or int): smallest value in the distribution
        max_value (float or int): largest value in the distribution
        size (int): size of distribution
        as_int (bool): specify whether values in the distribution are integers (defaults to False)
        plot_bins (int): if specified, a plot is generated for the distribution (if None, no plot 
        is generated; defaults to none)
        
    Returns:
        Normal distribution as numpy array
        Histogram of distribution (if plot_bins is given)
    """
   
    std_norm = np.random.normal(mu, sigma, size)
    minimum, maximum = np.min(std_norm), np.max(std_norm)
    a = std_norm - minimum
    b = a/np.max(a)
    c = b*(max_value-min_value)
    d = c + min_value
    if as_int:
        d2 = d.astype(int)
    else:
        d2 = d
    if plot_bins:
        plt.hist(d2, plot_bins, density=True)
        plt.show()
    else:
        pass
    return d2