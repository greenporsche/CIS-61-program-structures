def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.
    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    n = -1
    def fib():
        nonlocal n
        n += 1
        
        return fibonacci(n)
    
    return fib

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)