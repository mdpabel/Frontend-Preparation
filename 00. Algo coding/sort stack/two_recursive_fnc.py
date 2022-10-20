def sortStack(stack):
    """
    -5 2 -2 4 3 1
    [-5,-2,2,3,4]
    [-5,-2,2,3] 4 1

    """
    if len(stack) == 0:
        return stack

    top = stack.pop()
    sortStack(stack)

    insert(stack, top)

    return stack


def insert(stack, item):
    if len(stack) == 0 or stack[-1] <= item:
        stack.append(item)
        return
    top = stack.pop()
    insert(stack, item)
    stack.append(top)
