class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        nrow = len(matrix)
        ncol = len(matrix[0])
        s, l = 0, nrow * ncol - 1

        while s <= l:
            mid = (s + l)//2
            row = mid // ncol
            col = mid % ncol
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                s = mid + 1
            else:
                l = mid - 1
        return False