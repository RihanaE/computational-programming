class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        mid = 0
        
        while l <= r:
            mid = l + (r - l)// 2
            
            if nums[mid] < target:
                l = mid + 1
                
            elif nums[mid] == target:
                return mid
                
            else:
                r = mid - 1
                
            
        return l