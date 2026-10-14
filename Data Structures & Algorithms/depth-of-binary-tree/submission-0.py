# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        node = root

        if node is None:
            return 0
        
        max_depth_left = 1 + self.maxDepth(node.left)
        max_depth_right = 1 + self.maxDepth(node.right)

        return max(max_depth_left, max_depth_right)
