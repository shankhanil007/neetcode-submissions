# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(curr, cmax):
            if not curr:
                return 0

            res = 0
            if curr.val >= cmax:
                res = 1
                cmax = curr.val

            res += dfs(curr.left, cmax)
            res += dfs(curr.right, cmax)
            return res

        
        return dfs(root, -float('inf'))