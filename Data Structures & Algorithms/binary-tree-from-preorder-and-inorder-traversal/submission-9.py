# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        hmap = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(l, r):
            if l > r:
                return None

            root = preorder[self.pre_idx]
            root = TreeNode(root)
            self.pre_idx += 1

            in_idx = hmap[root.val]
            root.left = helper(l, in_idx-1)
            root.right = helper(in_idx+1, r)

            return root

        return helper(0, len(preorder)-1)