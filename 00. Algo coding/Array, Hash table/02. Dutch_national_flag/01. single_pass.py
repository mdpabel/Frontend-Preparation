class Solution:
    def sortColors(self, nums: List[int]) -> None:
        pivot = 1
        n = len(nums)
        
        smaller = 0
        for j in range(n):
            if pivot > nums[j]:
                nums[smaller], nums[j] = nums[j], nums[smaller]
                smaller += 1
        
        larger = n - 1
        for j in reversed(range(n)):
            if nums[j] > pivot:
                nums[larger], nums[j] = nums[j], nums[larger]
                larger -= 1
        
        