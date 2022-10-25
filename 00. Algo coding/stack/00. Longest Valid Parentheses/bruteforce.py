class Solution:
    def isValid(self, s):
        stack = []

        for item in s:
            if item == "(":
                stack.append("(")
            else:
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        return stack == []

    def longestValidParentheses(self, s: str) -> int:
        """
        ")()())"

        [)]
        c = 2
        l = 2
        """
        longest = 0
        n = len(s)

        for i in range(n):
            for j in range(i+2, n + 1):
                sub = s[i:j]
                if self.isValid(sub):
                    longest = max(longest, j - i)
        return longest
