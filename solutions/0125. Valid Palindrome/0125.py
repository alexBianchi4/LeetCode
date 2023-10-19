# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:        
        l, r = 0, len(s)-1
        while l < r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                    return False
            l+=1
            r-=1            
        return True
    
    # def isAlphaNumeric(char):
    #     return ((ord('A') <= ord(char) and ord(char) <= ord('Z')) or
    #         (ord('a') <= ord(char) and ord(char) <= ord('z')) and
    #         (ord('0') <= ord(char) and ord(char) <= ord('9')))