class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        ") ( ) ( ) )"
         0 1 2 3 4 5

        [0]
        max = 4

        "( ( ( ) )"
         0 1 2 3 4
        [0 , 1, 4]
        m = 2


        """
        stack = [-1]
        longest = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    longest = max(longest, i - stack[-1])
        return longest
