class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        vertical_element = 0

        for i in range(len(matrix) - 1):
            if target == matrix[i][0]:
                return True
            elif target > matrix[i][0] and target < matrix[i+1][0]:
                vertical_element = i
                break
            else:
                vertical_element = i + 1
        
        left = 0
        right = len(matrix[0]) - 1
        
        while left <= right:
            mid = (right + left) // 2
            if target == matrix[vertical_element][mid]:
                return True
            elif target > matrix[vertical_element][mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
