class Solution(object):
    def searchMatrix(self, matrix, target):

        m = 0

        for i in range(len(matrix) - 1):
            if target == matrix[i][0]:
                return True
            elif target > matrix[i][0] and target < matrix[i+1][0]:
                m = i
                break
            else:
                m = i + 1
        
        left = 0
        right = len(matrix[0]) - 1
        
        while left <= right:
            mid = (right + left) // 2
            if target == matrix[m][mid]:
                return True
            elif target > matrix[m][mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
