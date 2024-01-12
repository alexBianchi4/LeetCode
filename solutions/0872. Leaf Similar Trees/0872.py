# Time complexity: O(n)
# Space complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node == None:
                return []
            if node.left == None and node.right == None:
                return [node.val]
            left = dfs(node.left)
            right = dfs(node.right)
            left.extend(right)
            return left

        return dfs(root1) == dfs(root2)