# Time complexity : O(n)
# Space complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = []
        best = 0
        l = r = 0
        while r < len(s): 
            print(r, chars)           
            while s[r] in chars:
                chars.pop(0)
                l+=1
            chars.append(s[r])            
            best = max(best, len(chars))
            r+=1            
        return best