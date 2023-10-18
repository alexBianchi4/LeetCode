# Time Complexity : O(n)
# Space Complexity: O(1) as problem states output array does not count

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)        
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]

        postfix = 1
        for j in range(len(nums)-2, -1, -1):
            postfix *= nums[j+1]
            answer[j] *= postfix
        
        return answer

# Two pass strategy
# first pass, go left to right filling the array with the prefix up to each element i
# second pass, go right to left multiplying i by the postfix calculated up to that index
# finally multiply the elements of the two arrays to get the answer


# Time Complexity : O(n)
# Space Complexity: O(n)
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer = [1] * len(nums)
#         aux = [1] * len(nums)
#         for i in range(1, len(nums)):
#             answer[i] = answer[i-1] * nums[i-1]
        
#         for j in range(len(nums)-2, -1, -1):
#             aux[j] = aux[j+1] * nums[j+1]
                
#         answer = [x*y for x,y in zip(answer,aux)]
#         return answer