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
                return (0, True)

            lh, lb = dfs(curr.left)
            rh, rb = dfs(curr.right)
            currH = 1 + max(lh, rh)
            currB = False

            if abs(lh-rh) <= 1 and lb and rb:
                currB = True

            return currH, currB

        height, balanced = dfs(root)
        return balanced