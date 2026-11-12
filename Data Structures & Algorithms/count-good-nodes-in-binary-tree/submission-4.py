# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(curr, cmax):

            if not curr:
                return 0

            if curr.val >= cmax:
                res = 1
            else:
                res = 0

            cmax = max(curr.val, cmax)
            res += helper(curr.left, cmax)
            res += helper(curr.right, cmax)

            return res

        return helper(root, root.val)