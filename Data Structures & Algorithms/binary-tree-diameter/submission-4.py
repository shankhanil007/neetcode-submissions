# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

diameter = -1

class Solution:

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
        
    #     if root == None:
    #         return 0

    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

    #     if not root:
    #         return 0
        
    #     leftHght = self.maxDepth(root.left)
    #     rightHght = self.maxDepth(root.right)
    #     curDiam = leftHght + rightHght

    #     return max(curDiam, max(self.diameterOfBinaryTree(root.left),
    #               self.diameterOfBinaryTree(root.right)))


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.res = 0. ## IMP member variable of the class

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)
            diam = left + right
            self.res = max(diam, self.res)  ## Updation is important

            return 1 + max(left, right)

        dfs(root)
        return self.res
        

