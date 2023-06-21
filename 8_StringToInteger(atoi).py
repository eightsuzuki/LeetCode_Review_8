# n = len(s)
# time: O(n)
# space: O(1)

from typing import List

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        num = []
        s = s.strip()
        
        for i in range(len(s)):
            if s[i].isnumeric():
                num.append(s[i])
            elif s[i] in ['-', '+']:
                if num:
                    break
                num.append(s[i])
            else:
                break
        
        if num:
            if len(num) == 1 and not num[0].isnumeric():
                return 0
            num = int(''.join(num))
            if num >= 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif num <= -2 ** 31:
                return -2 ** 31
            return num
            
        return 0