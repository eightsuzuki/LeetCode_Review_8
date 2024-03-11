# Q is the number of queries, V is the number of vertices, E is the number of equations. 
# time: O(Q * (V + E))
# space: O(E + V)

from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        res = []
        
        for equation, value in zip(equations, values):
            dividend, divisor = equation
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1/value 
        
        
        def helper(start, end, total, visited):
            if start not in graph:
                return -1
            
            visited.add(start)
            
            if start == end:
                return total
            
            for connection, value in graph[start].items():
                if connection in visited:
                    continue
                    
                visited.add(connection)
                result = helper(connection, end, total*value, visited)
                if result != -1:
                    return result
                
            return -1
        
        for dividend, divisor in queries:
            result = helper(dividend, divisor, 1, set())
            res.append(result)
        
        return res