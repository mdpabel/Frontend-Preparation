class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        def swap(nums, i, j):
            nums[i], nums[j] = nums[j], nums[i]
        
        def sortColorsHelper(nums, left, right):
            
            if left >= right:
                return
            
            pivotIdx = left
            startIdx = left + 1
            endIdx = right
            
            while startIdx <= endIdx:
                if nums[startIdx] > nums[pivotIdx] and nums[endIdx] < nums[pivotIdx]:
                    swap(nums, startIdx, endIdx)
                
                if nums[startIdx] <= nums[pivotIdx]:
                    startIdx += 1
                
                if nums[endIdx] >= nums[pivotIdx]:
                    endIdx -= 1
                    
            swap(nums, pivotIdx, endIdx)
            
            sortColorsHelper(nums, pivotIdx, endIdx - 1)
            sortColorsHelper(nums, endIdx + 1, right)
            
        
        
            
        
        sortColorsHelper(nums, 0, len(nums)-1)
        
