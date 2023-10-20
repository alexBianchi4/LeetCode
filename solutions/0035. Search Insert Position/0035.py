# Time Complexity : O(logn)
# Space Complexity: O(1)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1        
        while l <= r:            
            m = (l+r)//2            
            if nums[m] < target:
                l = m+1                
            elif nums[m] > target:
                r = m-1                
            else:
                return m        
        return l