def isValid(str):
    if str == "":
        return True
    simplifiedStr = str.replace("()", "").replace("{}", "").replace("[]", "")
    if simplifiedStr == str:
        return False
    return isValid(simplifiedStr)


s = "()"
s = "()[]{}"
s = "(]"
print(isValid(s))
