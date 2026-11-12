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
                return 0, True
            if not curr.left and not curr.right:
                return 1, True
            
            leftHeight, leftBalanced = dfs(curr.left)
            rightHeight, rightBalanced = dfs(curr.right)

            currBalanced = False
            if (abs(leftHeight - rightHeight) <= 1) and leftBalanced and rightBalanced:
                 currBalanced = True
                
            currHeight = 1 + max(leftHeight, rightHeight)

            return currHeight, currBalanced

        rootHeight, rootBalanced = dfs(root)
        return rootBalanced