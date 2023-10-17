# Time complexity : O(n)
# Space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        lookup = {}
        for i, x in enumerate(nums):
            y = target - x
            j = lookup.get(y, -1) 
            if j > -1:
                return [i, j]
            lookup[x] = i