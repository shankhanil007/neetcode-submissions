# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        if not inorder:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        node = TreeNode(preorder[0])
    
        for inIdx, inVal in enumerate(inorder):
            if preorder[0] == inVal:
                if inIdx-1 >= 0:
                    node.left = self.buildTree(preorder[1:inIdx+1], inorder[0: inIdx])
                
                if inIdx+1 < len(inorder):
                    node.right = self.buildTree(preorder[inIdx+1:], inorder[inIdx+1: ])
                    
        return node

