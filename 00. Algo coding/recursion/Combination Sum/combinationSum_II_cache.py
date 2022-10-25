class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """ 10,1,2,7,6,1,5 8
        1, 1, 2, 5, 6, 7, 8, 10

        [1] -> [1,1] -> [1,1,2] -> [1,1,2,5]
                     -> [1,1,5] -> [1,1,5,6]
                     -> [1,1,6]
             ->[1,2,5]
        [1]

        """
        candidates.sort()

        def generateCombinationSum(i, combination, s, cache):
            nonlocal combinations
            if s == target:
                if combination not in combinations:
                    combinations.append(combination)
                return
            if s > target or i >= len(candidates):
                return

            if i in cache and cache[i] == combination:
                return
            else:
                cache[i] = combination

            generateCombinationSum(
                i+1, combination + [candidates[i]], s + candidates[i], cache)
            generateCombinationSum(i+1, combination, s, cache)

        combinations = []
        cache = {}
        generateCombinationSum(0, [], 0, cache)

        print(cache)

        return combinations
