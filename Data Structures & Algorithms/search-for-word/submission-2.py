class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        nrows = len(board)
        ncols = len(board[0])
        visited = [[0] * ncols for _ in range(nrows)]

        def helper(visited, idx, i, j):

            visited[i][j] = 1

            if board[i][j] == word[idx]:
                print(board[i][j], i, j, idx)
                if idx == len(word) - 1:
                    return True
                
                row_combs = [i-1, i, i, i+1]
                col_combs = [j, j-1, j+1, j]

                for itr in range(0, 4):
                    new_row = row_combs[itr]
                    new_col = col_combs[itr]
                    if new_row >= 0 and new_row < nrows and new_col >= 0 and new_col < ncols and visited[new_row][new_col] == 0:
                        if helper(visited, idx+1, new_row, new_col):  ## IMP to add if condition not just function call
                            return True
            visited[i][j] = 0       ## IMP to backtrack and clean up
            return False


        for i in range(0, nrows):
            for j in range(0, ncols):
                if helper(visited, 0, i, j):
                    return True

        return False
