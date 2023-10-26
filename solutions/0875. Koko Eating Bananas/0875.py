# Time Complexity : O(nlogn)
# Space Complexity: O(1)

from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            k = (l+r) // 2
            elapsed = sum([ceil(pile/k) for pile in piles])
            if elapsed > h:
                l = k + 1
            else:
                r = k - 1
        return l