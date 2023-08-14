# n = len(path)
# time: O(n)
# space: O(n)

from typing import List

class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []

        for component in path.split('/'):
            if component == '..':
                if s:
                    s.pop()
            elif not component:
                continue
            elif component == '.':
                continue
            else:
                s.append(component)

        return '/' + '/'.join(s)