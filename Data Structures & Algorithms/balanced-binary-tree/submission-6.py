# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(curr):
            if not curr:
                return (True, 0)

            lb, lh = dfs(curr.left)
            rb, rh = dfs(curr.right)
            ch = 1 + max(lh,rh)
            cb = False
            if lb and rb and abs(lh-rh) <= 1:
                cb = True

            return cb, ch

        balanced, height =  dfs(root)
        return balanced
