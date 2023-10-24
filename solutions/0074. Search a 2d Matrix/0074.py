#Time Complexity : O(logn + logm) = O(lognm)
#Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find the row that the value could be in
        t, b = 0, len(matrix)-1 # num rows
        row = 0
        while t <= b:
            m = (t+b)//2
            if matrix[m][0] <= target and matrix[m][-1] >= target:
                row = m
                break
            elif matrix[m][0] <= target:
                t = m+1
            else:
                b = m-1
        # find the col        
        l, r = 0, len(matrix[0])-1 # num cols
        while l <= r:
            m = (l+r)//2
            if matrix[row][m] < target:
                l = m+1
            elif matrix[row][m] > target:
                r = m-1
            else:
                return True        
        return False