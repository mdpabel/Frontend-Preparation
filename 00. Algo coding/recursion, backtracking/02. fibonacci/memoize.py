def getNthFib(n, cache={1: 0, 2: 1}):
    if n in cache:
        return cache[n]

    cache[n] = getNthFib(n - 1) + getNthFib(n - 2)
    return cache[n]
