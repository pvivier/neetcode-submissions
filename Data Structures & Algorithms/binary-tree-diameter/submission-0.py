# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.get_height_and_diameter(root)[1]

    def get_height_and_diameter(self, root: Optional[TreeNode]) -> list:
        node = root

        if node is None:
            return [0, 0]
        
        height_left, diam_left = self.get_height_and_diameter(node.left)
        height_right, diam_right = self.get_height_and_diameter(node.right)
        height_node = max(height_left, height_right)
        diam_node = max((height_left + height_right), diam_left, diam_right)
        
        return height_node+1, diam_node






