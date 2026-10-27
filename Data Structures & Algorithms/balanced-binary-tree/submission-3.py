# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def length_balanced(self, root):
        if not root:
            return 0
        else:
            left = self.length_balanced(root.left) + 1
            right = self.length_balanced(root.right) +1
            if left <0  or right < 0:
                return -50
            if abs(left - right) <= 1:
                return max(left, right)
            else:
                return -50

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        n = self.length_balanced(root)
        if n < 0:
            return False
        return True


