# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def test_subtree(self, root, subroot):
        
        if (not root and subroot) or (root and not subroot):
            return False
        if not root and not subroot:
            return True
        print("we are now checking with root " + str(root.val))
        if root.val != subroot.val:
            return False
        if root.val == subroot.val:
            return self.test_subtree(root.left, subroot.left) and self.test_subtree(root.right, subroot.right)
        
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if (not root and subroot) or (root and not subroot):
            return False
        if not root and not subroot:
            return True
        if self.test_subtree(root, subroot):
            print("subtree found at root " + str(root.val))
            return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)