def flatten(lst):
    """Returns a flattened version of lst.
    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    flattened = []
    for i in lst:
        if type(i) != list:
            flattened.append(i)
        else:
            flattened.extend(flatten(i))
    return flattened