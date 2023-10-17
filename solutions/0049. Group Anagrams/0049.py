# Time complexity : O(m*n)
# Space complexity: O(m)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        results = {}

        for string in strs:            
            # all chars are lowercase English letters
            vctr = [0] * 26
            for char in string:
                i = ord(char) - ord('a')
                vctr[i] += 1
            key = tuple(vctr)            
            if key in results:
                results[key].append(string)
            else:
                results[key] = [string]

        return list(results.values())

# could also just use the sorted string chars as a key i.e., results[''.join(sorted(string))].append(string)
# but this is O(m * nlogn)