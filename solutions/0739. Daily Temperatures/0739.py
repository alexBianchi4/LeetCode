# Time Complexity : O(n)
# Space Complexity: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # (temp, index)
        for i, temp in enumerate(temperatures):                        
            while stack and temp > stack[-1][0]:
                tempPrev, tempIndex = stack.pop()
                ans[tempIndex] = i-tempIndex      
            stack.append((temp, i))
        return ans