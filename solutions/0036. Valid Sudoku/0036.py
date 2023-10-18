# Time Complexity : O(n^2)
# Space Complexity: O(n*m) = O(n^2)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # keep track of computed rows, cols, boxes
        rows = {i:set() for i in range(9)} # key: row #
        cols = {j:set() for j in range(9)} # key: col #
        boxes = {(i,j):set() for j in range(3) for i in range(3)} # key: (row//3, col//3)

        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element == '.':
                    continue
                if element in rows[i] or element in cols[j] or element in boxes[(i//3,j//3)]:
                    return False
                rows[i].add(element)
                cols[j].add(element)
                boxes[(i//3,j//3)].add(element)                
        return True