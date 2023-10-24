"""
This script contains all functions

The following guidelines must be implemented for best practices:

-> Include Comment after declaring a function, this will act as
docstring when this functions is called
-> Run Flake8 after every commit
-> Run black after every commit

TODO : Log errors

"""
import pandas as pd


def normalize_json(file):
    """
    This function flattens the json and returns the output
    """
    tmp = pd.json_normalize(file)
    return tmp

def flatten_data(y):
    """
    This function flattens a json object with any structure.
    The code recursively extracts values out of the object into a flattened dictionary.
    """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    ans = pd.json_normalize(out)
    return ans