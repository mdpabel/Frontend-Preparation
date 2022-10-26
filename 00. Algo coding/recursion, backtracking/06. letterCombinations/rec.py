DIGITAL_LETTERS = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """ 23
        a -> ad
          -> ae
          -> af
        b -> bd
          -> be
          -> bf

        """
        if len(digits) == 0:
            return []

        def helper(i, currentCombination):
            nonlocal combinations
            if i >= len(digits):
                combinations.append(currentCombination)
                return

            digit = digits[i]
            letters = DIGITAL_LETTERS[digit]

            for letter in letters:
                helper(i + 1, currentCombination + letter)

        combinations = []

        helper(0, "")

        return combinations
