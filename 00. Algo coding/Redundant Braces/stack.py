def braces(s):
    stack = []

    for item in s:
        if item in "+-*/(":
            stack.append(item)
        elif item == ")":
            lastItem = stack.pop()
            if lastItem == "(":
                return True
            while "(" != stack.pop():
                continue
    return False
