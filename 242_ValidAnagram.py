# n = len(s), m = len(t)
# time: O(n+m)
# space: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mydict = {}

        for i in s:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        
        for i in t:
            if i in mydict:
                mydict[i] -= 1
                if mydict[i] == 0:
                    del mydict[i]
            else:
                return False
        
        if not mydict:
            return True
        
        return False