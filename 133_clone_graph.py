# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class CloneGraph:
    def clone_graph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited, from_node_to_node = set(), {}
        def dfs(curr: 'Node')->None:
            if curr.val in visited:
                return None
            visited.add(curr.val)
            if curr not in from_node_to_node:
                from_node_to_node[curr] = Node(curr.val)
            for neighbor in curr.neighbors:
                if neighbor not in from_node_to_node:
                    from_node_to_node[neighbor] = Node(neighbor.val)
                from_node_to_node[curr].neighbors.append(from_node_to_node[neighbor])
                dfs(neighbor)
        dfs(node)
        return from_node_to_node[node]
