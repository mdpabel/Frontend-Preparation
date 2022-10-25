def getNthFib(n):
    """
    (n-1) + (n-2)
    2
    1 + 0 = 1
    6
    5 + 4

    """
    if n == 2:
        return 1
    if n == 1:
        return 0
    return getNthFib(n - 1) + getNthFib(n - 2)
