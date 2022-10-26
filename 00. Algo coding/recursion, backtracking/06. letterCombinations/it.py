class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """ 23
         -> ""
        2 -> "a", "b", "c"
        3 -> ad, ae, af, bd, be, bf, cd, ce, cf
        """
        if len(digits) == 0: return []
        
        DIGITAL_LETTERS = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
                   
        letterCombinations = [""]
        
        for digit in digits:
            letters = DIGITAL_LETTERS[digit]
            currentCombinations = []
            for letter in letters:
                for letterCombination in letterCombinations:
                    currentCombinations.append(letterCombination + letter)
            letterCombinations = currentCombinations
            
        return letterCombinations