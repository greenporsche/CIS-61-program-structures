from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.
    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """

    if b < 0:
        f = lambda a, b: a - b
    else:
        f = lambda a, b: a + b

    return f(a, b)