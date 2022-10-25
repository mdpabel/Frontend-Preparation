class Solution:
    def combinationSum2(self, candidates, target: int):
        """ 10,1,2,7,6,1,5 8
        1, 1, 2, 5, 6, 7, 8, 10

        [1] -> [1,1] -> [1,1,2] -> [1,1,2,5]
                     -> [1,1,5] -> [1,1,5,6]
                     -> [1,1,6]
             ->[1,2,5]
        [1]

        """
        candidates.sort()

        def generateCombinationSum(i, combination, s):
            nonlocal combinations
            if s == target:
                if combination not in combinations:
                    combinations.append(combination.copy())

            if s > target or i >= len(candidates):
                return

            generateCombinationSum(
                i+1, combination + [candidates[i]], s + candidates[i])
            generateCombinationSum(i+1, combination, s)
            return None

        combinations = []

        generateCombinationSum(0, [], 0)

        return combinations
