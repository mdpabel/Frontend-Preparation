class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """ [1,2,3]
        []
        [1]i=0 -> [1, 2]i=1 -> [1,2,3]i=2 # combination to keep 1
                               [1,2]  
                  [1, 3]i=2
                  [1]
        [2]i=1 -> [2,3]i=2 # combination to keep 2
                  [2]
        [3]i=3 # combination to keep 3
        """
        n = len(nums)
        subsets = []

        def generate_subsets(i, li):
            subsets.append(li.copy())

            for i in range(i, n):
                li.append(nums[i])
                generate_subsets(i+1, li)
                li.pop()
            # return None

        generate_subsets(0, [])

        return subsets

    """
    subsets = [[],[1, 2].[1,2,3], [1,3] ]
    li = [2]
    """
