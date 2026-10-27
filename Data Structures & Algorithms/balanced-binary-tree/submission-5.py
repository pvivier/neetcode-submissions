# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def balanced_depth(self, root):
        if not root:
            return [True, 0]
        left = self.balanced_depth(root.left)[1] +1
        if root.right is None:
            print(root.val)
        right = self.balanced_depth(root.right)[1] + 1
        
        if left == 0 or right == 0:
            return [False, -1]
        if abs(left - right) <= 1:
            return [True, max(left,right)]
        return [False, -1]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        check = self.balanced_depth(root)
        return check[0]
        


