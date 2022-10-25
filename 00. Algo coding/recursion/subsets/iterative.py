class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ [1,2,3]

        subsets = [[]]
        1 -> [] ->withoutItem, [1] ->withItem

        1, 2, 3

        1 -> [], [1] 
        2 -> [], [2], [1], [1,2]
        3 -> [], [3], [2], [2,3] [1], [1,3], [1,2], [1,2,3]

        """
        subsets = [[]]

        for num in nums:
            currentSubsets = []
            for subset in subsets:
                currentSubsets.append(subset + [])
                currentSubsets.append(subset + [num])
            subsets = currentSubsets

        return subsets
