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

            if (l and not r) or (r and not l) or (l.val != r.val):
                return False

            left = dfs(l.left, r.left)
            right = dfs(l.right, r.right)
            
            return left and right 

        own = dfs(root, subRoot)
        
        if own :
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


