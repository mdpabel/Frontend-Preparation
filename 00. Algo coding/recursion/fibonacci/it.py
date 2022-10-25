def getNthFib(n):
    if n == 1:
        return 0
    first, second = 0, 1

    fib = first + second

    for _ in range(n - 2):
        fib = first + second
        first, second = second, fib

    return fib
