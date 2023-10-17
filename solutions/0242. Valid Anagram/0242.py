# Time complexity : O(n)
# Space complexity: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        for char in countS:
            if countT.get(char, 0) != countS[char]:
                return False
        return True
    
# if you uncomment the first return statement then:
#  Time complexity : O(nlogn)
#  Space complexity: O(n) or O(1) depending on sort alg.