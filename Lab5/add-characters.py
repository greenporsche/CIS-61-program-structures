def add_characters(w1, w2):
    """
    Takes in w1 and w2, where w1 is a substring of w2. It should return a string containing the characters you need to add to w1 to get w2.
    >>> add_characters("coy", "cacophony")
    'acphon'
    """
    if len(w1) == 0:
        return w2[1:]
    elif w1[0] != w2[0]:
        return w2[0] + add_characters(w1, w2[1:])
    else:
        return add_characters(w1[1:], w2[1:])