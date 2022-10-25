class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ [1,2,3]

        [1,2,3]
        [1,2]
        [1,3]
        [1]
        [2,3]
        [2]
        [3]

        genSub(1, [1]) ->genSub(2, [1, 2]) -> genSub(3, [1,2,3]) 
                                           -> genSub(3, [1,2])
                       ->genSub(2, [1]) -> genSub(3, [1, 3])
                                        -> genSub(3, [1])
        genSub(1, []) -> genSub(2, [2]) -> genSub(3, [2, 3])
                                        -> genSub(3, [2])
                       ->genSub(2, []) -> genSub(3, [3])
        """
        n = len(nums)
        subsets = []

        def generate_subsets(i, li):
            if i == n:
                subsets.append(li)
                return
            generate_subsets(i + 1, li + [nums[i]])
            generate_subsets(i + 1, li)

        generate_subsets(0, [])

        return subsets
