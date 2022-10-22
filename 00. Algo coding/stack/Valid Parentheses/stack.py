def isValid(str):
    stack = []
    validParentheses = {
        "(": ")",
        "{": "}",
        "[": "]"
    }

    for parentheses in s:
        if parentheses in validParentheses:
            stack.append(parentheses)
        else:
            if stack == [] or validParentheses[stack.pop()] != parentheses:
                return False
    return stack == []


s = "()"
s = "()[]{}"
s = "(]"
print(isValid(s))
