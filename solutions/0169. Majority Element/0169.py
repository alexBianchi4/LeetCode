# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        m = len(nums) // 2
        for num in nums:
            count = counts.get(num,0) + 1
            if count > m:
                return num
            counts[num] = count