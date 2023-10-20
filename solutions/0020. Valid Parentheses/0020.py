# Time Complexity : O(n)
# Space Complexity: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {'(':')','{':'}','[':']'}
        for char in s:
            # open bracket
            if char in mapping:
                stack.insert(0,char)
            # close bracket
            else:
                if len(stack) == 0 or mapping[stack.pop(0)] != char:
                    return False
        
        return True if len(stack) == 0 else False