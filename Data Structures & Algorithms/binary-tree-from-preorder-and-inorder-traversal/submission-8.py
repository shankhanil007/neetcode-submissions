class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # Precompute indices of inorder values for O(1) lookups
        hmap = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def helper(l, r):
            
            # Base case: no elements left in this subtree
            if l > r:
                return None

            # Pick current root from preorder traversal
            root = preorder[self.pre_idx]
            root = TreeNode(root)
            self.pre_idx += 1

            # Get index of root in inorder array
            root_idx = hmap[root.val]

            # Recursively build left and right subtrees using boundary pointers
            root.left = helper(l, root_idx - 1)
            root.right = helper(root_idx + 1, r)

            return root

        return helper(0, len(inorder) - 1)