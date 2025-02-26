def group_by(seq, fn): 
    """ 
    >>> group_by([12, 23, 14, 45], lambda p: p // 10) 
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(list(range(-3, 4)), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    fn_seq = {}
    for i in seq:
        fn_seq[i] = fn(i)

    new_dict = {}
    values = fn_seq.keys()
    outputs = []
    for i in sorted(values, key=fn):
        if outputs.count(fn(i)) == 0:
            outputs.append(fn(i))
            new_dict[fn(i)] = [i]
        else:
            new_dict[fn(i)].append(i)
    return new_dict