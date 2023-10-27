from collections import deque
from typing import Deque, Optional


class TreeNode:
    def __init__(
            self, 
            val: int = 0, 
            left: Optional["TreeNode"] = None, 
            right: Optional["TreeNode"] = None
    ):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        stack = deque()
        stack.append(root)
        deserialized_data = []
        while stack:
            cur = stack.pop()
            if cur:
                deserialized_data.append(str(cur.val))
                stack.append(cur.right)
                stack.append(cur.left)
            
            else:
                deserialized_data.append("#")
        
        return " ".join(deserialized_data)


    def deserialize(self, data: str) -> Optional[TreeNode]:
        deserialized_data = data.split(" ")
        queue = deque(deserialized_data)
        root = self.deserialize_recursive(queue)
        return root
    
    def deserialize_recursive(self, queue: Deque[str]) -> Optional[TreeNode]:
        if not queue:
            return None

        next_node_val = queue.popleft()
        if next_node_val == "#":
            return None

        root = TreeNode(next_node_val)
        root.left = self.deserialize_recursive(queue)
        root.right = self.deserialize_recursive(queue)
        return root
