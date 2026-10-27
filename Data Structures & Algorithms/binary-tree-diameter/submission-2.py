# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def length_and_diameter(self, root):
        if not root:
            return [0,0]
        if (not root.left) and (not root.right):
            return [0,0]
        if (root.left) and (not root.right):
            left_stats = self.length_and_diameter(root.left)
            return [left_stats[0]+1, max(left_stats[0]+1, left_stats[1])]
        if (not root.left) and (root.right):
            right_stats = self.length_and_diameter(root.right)
            return [right_stats[0]+1, max(right_stats[0]+1, right_stats[1])]
        if root.left and root.right:
            left_stats = self.length_and_diameter(root.left)
            right_stats = self.length_and_diameter(root.right)
            
            return [max(left_stats[0], right_stats[0])+1, max(left_stats[0] + right_stats[0] + 2, max(left_stats[1], right_stats[1]))]

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        root_stats = self.length_and_diameter(root)

        return max(root_stats)

        