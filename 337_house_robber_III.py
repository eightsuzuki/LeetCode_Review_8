from typing import Optional, List


class TreeNode:
    def __init__(
            self,
            val: int = 0,
            left: Optional["TreeNode"] = None,
            right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right



class Robber:
    def calc_max(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))
    
    def dfs(self, node):
        if not node:
            return (0, 0)
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        return (node.val + left[1] + right[1], max(left[0], left[1]) + max(right[0], right[1]))