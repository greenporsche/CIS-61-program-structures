def newFunction(a, b):
    """
    >>> newFunction(3, 4)
    5
    >>> newFunction(8, 15)
    17
    >>> newFunction(5, 12)
    13
    """
    return int((a ** 2 + b ** 2) ** (1 / 2))