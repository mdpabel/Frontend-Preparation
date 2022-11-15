class Solution:
    def sortColors(self, nums: List[int]) -> None:
        pivot = 1
        n = len(nums)
        
        smaller, equal, larger = 0, 0, n - 1
        
        while equal <= larger:
            if nums[equal] < pivot:
                nums[smaller], nums[equal] = nums[equal], nums[smaller]
                smaller += 1
                equal += 1
            elif nums[equal] == pivot:
                equal += 1    
            else:
                nums[equal], nums[larger] = nums[larger], nums[equal]
                larger -= 1
