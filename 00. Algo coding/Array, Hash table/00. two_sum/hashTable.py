# Example
"""
nums = [2,7,11,15], target = 9
"""

# Solution
"""
To keep a record of the previous values and their indices we can use a dictionary.
"""

# Test case
"""
{
    2 : 0,

}
9 - 2 = 7
9 - 7 = 2

"""

# code


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            expected_num = target - nums[i]
            if expected_num in seen:
                return [seen.get(expected_num), i]
            else:
                seen[nums[i]] = i


# Verify
"""
{
    2 : 0,

}
9 - 2 = 7
9 - 7 = 2


"""

# Time and Space
"""
Time O(n)
Space O(n)
"""
