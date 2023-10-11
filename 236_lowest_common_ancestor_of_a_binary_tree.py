class TreeNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

# Recursive approach
# n = the number of nodes in the tree
# time: O(n)
# space: O(n)

class Solution1:
    def find_lowest_common_ancestor(self,
                                    root: 'TreeNode',
                                    p: 'TreeNode',
                                    q: 'TreeNode') -> 'TreeNode':
        """Function to find the lowest common ancestor (LCA) of two give nodes.
        LCA is defined between two nodes 'p' and 'q' as the lowest node in 'T'
        that has both 'p' and 'q' as descendants.
        
        Args:
            root (TreeNode): Root node of a given tree
            p, q (TreeNode): Descendants
        
        Returns:
            TreeNode: The lowest common ancestor of 'p' and 'q'
        """
        if not root or root is p or root is q:
            return root
        
        left = self.find_lowest_common_ancestor(root.left, p, q)
        right = self.find_lowest_common_ancestor(root.right, p, q)
        if left and right:
            return root
        
        if left:
            return left
        
        if right:
            return right

# Iterative approach
# n = The number of nodes in the tree
# time: O(n)
# space: O(n)

class Solution2:
    def find_lowest_common_ancestor(self,
                                    root: 'TreeNode',
                                    p: 'TreeNode',
                                    q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        from_node_to_parent = {root: None}

        while p not in from_node_to_parent or q not in from_node_to_parent:
            node = stack.pop()
            if node.left:
                from_node_to_parent[node.left] = node
                stack.append(node.left)
            if node.right:
                from_node_to_parent[node.right] = node
                stack.append(node.right)
            
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = from_node_to_parent[p]
        
        while q not in ancestors:
            q = from_node_to_parent[q]

        return q
