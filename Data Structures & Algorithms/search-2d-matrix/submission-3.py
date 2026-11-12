class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix)
        m = len(matrix[0])
        l, h = 0, (n * m)-1

        while l <= h:
            mid = (l+h)//2
            row = mid//m
            col = mid%m
            print(mid, row, col)
            if target < matrix[row][col]:
                h = mid - 1
            elif target > matrix[row][col]:
                l = mid + 1
            else:
                return True
        return False