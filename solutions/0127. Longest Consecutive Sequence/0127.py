# Time Complexity:  O(n)
# Space Complexity: O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for n in nums:
            # if the num 1 less than n is not in the hashset,
            #  then this is the start of a sequence
            if n - 1 not in nums:
                length = 1
                x = n+1
                while x in nums:
                    length += 1
                    x += 1
                longest = max(longest, length)
        return longest