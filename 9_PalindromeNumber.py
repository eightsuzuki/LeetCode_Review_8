# n = int(math.log10(x)) + 1 or n = xの桁数 
# time:  O(n) 
# space: O(1)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = x
        back = 0

        while x > 0:
            back = (back * 10) + (x % 10)
            x = x // 10
						
        return s == back

				
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#     	if x < 0 and x % 10 == 0:
# 	    	return False
	
#     	return str(x) == str(x)[::-1]