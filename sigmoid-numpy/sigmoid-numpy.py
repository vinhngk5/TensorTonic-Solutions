import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    func = lambda num: 1 / (1 + np.exp(-num))

    if isinstance(x, list):
        return [sigmoid(val) for val in x]

    return func(x)