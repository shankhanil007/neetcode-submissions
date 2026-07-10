# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root or not subRoot:
            return False

        def dfs(l, r):
            if l == r == None:
                return True

            if l and r and (l.val == r.val):
                return dfs(l.left, r.left) and dfs(l.right, r.right)
            
            return False

        if dfs(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


