from typing import Optional


class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left: Optional["TreeNode"] = None,
            right: Optional["TreeNode"] = None
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeAncestor:
    def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Funtction to find the lowest common ancestor
        Args:
            root(TreeNode): a binary search tree
            p(TreeNode): a binary search tree
            q(TreeNode): a binary search tree
        Returns:
            TreeNode: the lowest common ancestor
        """
        # V: the number of nodes
        # time: O(log(V))
        # space: O(1)

        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            
            elif cur.val < p.val and cur.val < q.val:
                cur = cur.right
            
            else:
                return cur

        raise ValueError(f'there is no ancestor in the root node')