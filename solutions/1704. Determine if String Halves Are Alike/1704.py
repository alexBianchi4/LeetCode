# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a','e','i','o','u'}
        l, r = 0, len(s)-1
        c1 = c2 = 0
        while l < r:
            if s[l].lower() in vowels:
                c1 += 1
            if s[r].lower() in vowels:
                c2 += 1
            l+=1
            r-=1
        return c1 == c2