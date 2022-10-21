def nextGreaterElement(array):
    """ [2, 5, -3, -4, 6, 7, 2]
        [5, -1, -1, -1, -1, -1]
        stack = [1]

        top = 2
        curr = 5

    """
    n = len(array)
    stack = []
    result = [-1 for _ in range(n)]

    for i in range(2 * n):
        circularIdx = i % n
        while stack and array[stack[-1]] < array[circularIdx]:
            top = stack.pop()
            result[top] = array[circularIdx]
        stack.append(circularIdx)
    return result
