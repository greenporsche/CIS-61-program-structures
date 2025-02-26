def is_prime(n, divisor = None):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False

    if divisor is None:
        divisor = 3


    if divisor > int(n**(1/2)):
        return True

    if n % divisor == 0:
        return False

    return is_prime(n, divisor + 2)