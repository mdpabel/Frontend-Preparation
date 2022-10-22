def sortStack(stack):
    if len(stack) <= 1:
        return stack

    valueone = stack.pop()
    sortStack(stack)
    valuetwo = stack.pop()

    if valueone > valuetwo:
        valueone, valuetwo = valuetwo, valueone

    stack.append(valueone)
    sortStack(stack)
    stack.append(valuetwo)

    return stack
