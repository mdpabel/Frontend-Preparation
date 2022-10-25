def productSum(array, depth=1):
    sum = 0
    for item in array:
        if type(item) == list:
            sum += productSum(item, depth + 1)
        else:
            sum += item
    return sum * depth
