def hailstone(n):
    """Print the hailstone sequence starting at n and return its length.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    k = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
            print(n)
        else:
            n = 3*n + 1
            print(n)
        k += 1
    return k