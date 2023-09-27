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


class MaxPathCalculator:
    def calculate_max_path_sum(self, root: Optional[TreeNode]) -> int:
        self.max_num = -float('inf')
        self.max_path_recursive(root)
        return self.max_num
    
    def max_path_recursive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left = max(0, self.max_path_recursive(root.left))
        right = max(0, self.max_path_recursive(root.right))
        cur_max = root.val + right + left
        self.max_num = max(self.max_num, cur_max)
        
        return max(root.val + left, root.val + right)
