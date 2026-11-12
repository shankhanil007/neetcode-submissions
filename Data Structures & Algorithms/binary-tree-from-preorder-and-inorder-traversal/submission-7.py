class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Precompute indices of inorder values for O(1) lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def helper(in_left, in_right):
            nonlocal pre_idx
            
            # Base case: no elements left in this subtree
            if in_left > in_right:
                return None

            # Pick current root from preorder traversal
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # Get index of root in inorder array
            in_idx = inorder_map[root_val]

            # Recursively build left and right subtrees using boundary pointers
            root.left = helper(in_left, in_idx - 1)
            root.right = helper(in_idx + 1, in_right)

            return root

        return helper(0, len(inorder) - 1)