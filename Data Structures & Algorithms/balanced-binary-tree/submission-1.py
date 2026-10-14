# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#run thru the tree top to bottom, do it in some symmetrical type of way,
#if your running height for every node is the same +-1, 


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        node = root
        


        if node is None:
            return True
        elif abs(self.compute_height(node.left) - self.compute_height(node.right)) <= 1:
            return (self.isBalanced(node.left) and self.isBalanced(node.right))
        else:
            return False


    def compute_height(self, node):
        if node is None:
            return 0
        height = 1 + max(self.compute_height(node.left), self.compute_height(node.right))
        return height

