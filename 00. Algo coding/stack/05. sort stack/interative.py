def sortStack(stack):
    tempStack = []
    while stack:
        top = stack.pop()
        tempStack.append(top)

    while tempStack:
        if len(stack) == 0 or tempStack[-1] >= stack[-1]:
            top = tempStack.pop()
            stack.append(top)
        else:
            top = tempStack.pop()
            while len(stack) and stack[-1] > top:
                top2 = stack.pop()
                tempStack.append(top2)
            stack.append(top)
    return stack
