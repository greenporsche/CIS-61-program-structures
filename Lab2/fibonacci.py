def fibonacciN(n):
    """Return the nth Fibonacci number.
    Fibonacci Numbers is a series of numbers in which each number is 
    the sum of the two preceding numbers
    >>> fibonacciN(5) # 1, 1, 2, 3, 5
    5
    >>> fibonacciN(7) 
    13
    """
    k = 0
    prev = 0
    curr = 1
    while k < n:
        next = prev + curr
        prev = curr
        curr = next
        k += 1
    return prev