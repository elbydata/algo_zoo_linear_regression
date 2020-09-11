import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class random_array:
    
    """
    Class description: an array of randomly generated numbers generated using the below functions.
    """
   
    def __init__(self,size,min_max=None,ints=False):
        
        """
        Creates an instance of the class random_array.
    
        Parameters:
            size (int): size of array
            min_max (tuple or list of floats or ints): specify the minimum and maximum values of the array 
            (defaults to None)
            ints (bool): specify whether values in the array are integers (defaults to False)
        
        Returns:
            Instantiation of the class random_array with given parameters
        """
        
        self.size = int(size)
        if min_max is None:
            self.min_value = None
            self.max_value = None
        elif (type(min_max) is tuple) or (type(min_max) is list) and len(min_max) == 2:
            self.min_value = int(min_max[0])
            self.max_value = int(min_max[1])
        else:
            self.min_value = None
            self.max_value = None            
        if ints is True:
            self.ints = True
        else:
            self.ints = False

    def generate_simple(self):
        
        """
        Generates a simple random array from the instantiation of the class random_array.
        """
        
        if bool(self.min_value and self.max_value):
            a = np.random.random(size=self.size)
            minimum, maximum = np.min(a), np.max(a)
            b = a - minimum
            c = b/np.max(b)
            d = c*(self.max_value-self.min_value)
            e = d + self.min_value
        else:
            e = np.random.random(size=self.size)
        if self.ints:
            s = e.astype(int)
        else:
            s = e
        return s

    def generate_normal(self):
        
        """
        Generates a normally distributed array from the instantiation of the class random_array.
        """         
        
        if bool(self.min_value and self.max_value): 
            a = np.random.normal(0, 1, self.size)
            minimum, maximum = np.min(a), np.max(a)
            b = a - minimum
            c = b/np.max(b)
            d = c*(self.max_value-self.min_value)
            e = d + self.min_value        
        else:
            e = np.random.normal(mu, sigma, self.size)
        if self.ints:
            s = e.astype(int)
        else:
            s = e
        return s    
    
    def generate_linear(self,m,c):
        
        """
        Generates a linear pair of arrays fromm the instantiation of the class random_array.
    
        Parameters:
            m (float or int): gradient of linear relationship
            c (float or int): y-intercept
        
        Returns:
            Linear pair of numpy arrays of random numbers
        """        
        
        if bool(self.min_value and self.max_value):
            a = np.random.random(size=self.size)
            minimum, maximum = np.min(a), np.max(a)
            b = a - minimum
            c = b/np.max(b)
            d = c*(self.max_value-self.min_value)
            x = d + self.min_value
        else:
            x = np.random.random(size=self.size)
        y = m*x + c
        if self.ints:
            sx = x.astype(int)
            sy = y.astype(int)
        else:
            sx = x
            sy = y
        return sx, sy            
