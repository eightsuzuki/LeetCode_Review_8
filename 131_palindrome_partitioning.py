# DFS (backtracking)
# n = len(s)
# time: O(n * 2^n)
# space: O(n)

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """Function to partition a string such that every 
        substring of the partition is a  palindrome.

        Args:
            s (str): A partitioned string

        Returns:
            list[list[str]]: All possible palindrome partitioning of s
        """
        res = []
        current_partition = []
        self.dfs(s, 0, res, current_partition)
        return res
    
    def dfs(self, s: list[str], start: int, res: list[list[str]],
            current_partition: list[str]) -> None:
        """Function to generate all possible substrings,
        and see if is is a palindrome.

        Args:
            s (str): Original partitioned string
            start (int): Start index of a substring
            res (list[list[str]]): Stores all palindrome partitionings
            current_partition (list[str])
                : Stores how 's' is partitioned currently
        """
        if start >= len(s):
            res.append(current_partition)
            return
        
        for end in range(start, len(s)):
            if self.is_palindrome(s, start, end):
                self.dfs(s, end + 1, res, current_partition + [s[start:end+1]])

    def is_palindrome(self, s: list[str], start: int, end: int) -> bool:
        """Function to check if a substring of 's' is a palindrome.

        Args:
            s (list[str]): Original string
            start (int): Start index of a substirng
            end (int): End index of a substring

        Returns:
            bool: True if a substring is palindrome, False otherwise
        """
        while start < end:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1

        return True
