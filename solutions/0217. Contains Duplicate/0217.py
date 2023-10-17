# Time complexity : O(n)
# Space complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = {}
        for num in nums:
            count = lookup.get(num,0)
            if count > 0:
                return True            
            lookup[num] = count + 1
        return False

# can also make a trade-off between time and space complexity by first sorting the array,
#  then moving two pointers to see if adjacent elements are the same
#  Time complexity:  O(nlogn)
#  Space complexity: O(1)