# Time complexity :  O(N^2)
# Space complexity:  O(N) - depending on sort, could be O(1)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        # no three +'ve triplets sum to zero
        if nums[0] > 0: 
            return results
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # early exit condition
            if nums[i] > 0:
                return results
            l, r = i + 1, len(nums) - 1
            # this is just 2Sum problem now
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if res < 0:
                    l += 1
                elif res > 0:
                    r -=1
                else:
                    results.append([nums[i], nums[l], nums[r]])
                    l += 1                    
                    while nums[l] == nums[l-1] and l < r:
                        l += 1                    
        return results