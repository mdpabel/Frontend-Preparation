
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def generatePermutations(nums, permutation):
            if len(nums) == 0 and len(permutation):
                permutations.append(permutation)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                newNum = nums[:i] + nums[i+1:]
                newPermutation = permutation + [nums[i]]
                generatePermutations(newNum, newPermutation)

        permutations = []
        generatePermutations(nums, [])
        return permutations
