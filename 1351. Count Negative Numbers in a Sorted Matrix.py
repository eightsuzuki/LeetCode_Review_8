class Solution(object):
    def countNegatives(self, grid):
        a = len(grid[0])
        count = 0
        i = 0
        j = 0

        while i < a and j < a:
            if grid[i][j] < 0:
                count += a - j
                i += 1
                j = 0
            else:
                j += 1
        return count
