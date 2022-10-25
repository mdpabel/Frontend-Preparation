
# Example
"""
nums = [2,7,11,15], target = 9
"""

# Solution
"""
nums[i] + nums[j] == target: return [i, j]
"""

# Test case
"""
2, 7, 11, 15
i
   j
"""

# code


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            first_num = nums[i]
            for j in range(i+1, n):
                second_num = nums[j]
                if first_num + second_num == target:
                    return [i, j]


# Verify
"""
2, 7, 11, 15

first_num = 2
second_num = 7

2 + 7 == 9
"""

# Time and Space
"""
Time O(n^2)
Space O(1)
"""
