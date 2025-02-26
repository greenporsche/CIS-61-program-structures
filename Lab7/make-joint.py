def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'
    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10
    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    result = withdraw(0, old_password)
    if type(result) == str:
        return result
    
    def j(balance, pass_attempt):
        if pass_attempt == old_password or pass_attempt == new_password:
            return withdraw(balance, old_password)
        else:
            return withdraw(balance, pass_attempt)
    return j


def make_withdraw(balance, password):
    num_attempts = 0
    attempts = []
    def withdraw(amount, pass_attempt):
        nonlocal balance
        nonlocal num_attempts
        nonlocal attempts

        if num_attempts >= 3:
            return f"Your account is locked. Attempts: {attempts}"

        if pass_attempt != password:
            attempts.append(pass_attempt)
            num_attempts += 1
            return "Incorrect password"
        
        if amount > balance:
           return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw