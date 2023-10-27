# Time complexity : O(n)
# Space complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

# can also make a trade-off between time and space complexity by first sorting the array,
#  then moving two pointers to see if adjacent elements are the same
#  Time complexity:  O(nlogn)
#  Space complexity: O(1)