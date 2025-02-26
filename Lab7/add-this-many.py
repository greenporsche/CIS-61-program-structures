def add_this_many(x, el, lst): 
    """ Adds el to the end of lst the number of times x occurs in lst. 
    >>> lst = [1, 2, 4, 2, 1]  
    >>> add_this_many(2, 5, lst) 
    >>> lst 
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, lst) 
    >>> lst
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    n = lst.count(x)
    for i in range(n):
        lst.append(el)