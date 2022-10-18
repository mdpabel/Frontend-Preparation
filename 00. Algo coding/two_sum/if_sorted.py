#-------------------IF THE ARRAY ALREADY SORTED-------------------------#

# Example
"""
nums = [2,7,11,15], target = 9
"""

# Solution
"""
nums[left] + nums[right] == target: return [i, j]
"""

# Test case
"""
left = 0
right = 3

2, 7, 11, 15

2 + 15 = 17
2 + 11 = 13
2 + 7 = 9

"""

# code


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left, right]

            if current_sum > target:
                right -= 1
            else:
                left += 1


# Verify
"""
2, 7, 11, 15

2 + 15 = 17
2 + 11 = 13
2 + 7 = 9

"""

# Time and Space
"""
Time O(n)
Space O(1)
"""
