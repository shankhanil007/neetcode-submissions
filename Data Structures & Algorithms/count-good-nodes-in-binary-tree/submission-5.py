# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0

        def dfs(curr, cmax):
            if not curr:
                return
            
            if curr.val >= cmax:
                self.good += 1
                cmax = curr.val

            dfs(curr.left, cmax)
            dfs(curr.right, cmax)

        dfs(root, -float('inf'))
        return self.good