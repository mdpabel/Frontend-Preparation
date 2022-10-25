class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """[1,2,2]
        []
        1 -> [], [1]
        2 -> [], [2], [1], [1,2]
        2 -> [], [2], [2], [2,2], [1], [1,2], [1,2,2]

        """
        nums.sort()
        subsets = [[]]

        for num in nums:
            current_subsets = []
            last_subsets = []
            for subset in subsets:
                sub1 = subset + []
                sub2 = subset + [num]
                if sub1 not in last_subsets:
                    current_subsets.append(sub1)
                if sub2 not in last_subsets:
                    current_subsets.append(sub2)
                last_subsets = []
                last_subsets.append(sub1)
                last_subsets.append(sub2)
            subsets = current_subsets
        return subsets
