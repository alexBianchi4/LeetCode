# Time complexity : O(n)
# Space complexity: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        stairs = [1] * (n+1)
        for i in range(2, n+1):
            stairs[i] = stairs[i-1] + stairs[i-2]
        return stairs[n]