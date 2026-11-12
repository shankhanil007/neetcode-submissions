class Solution:
    def solve(self, board: List[List[str]]) -> None:

        nrows = len(board)
        ncols = len(board[0])
        visited = set()
        row_delta = [0, -1, 1, 0]
        col_delta = [-1, 0, 0, 1]

        def dfs(curr_row, curr_col):

            visited.add((curr_row, curr_col))
            board[curr_row][curr_col] = 'SS'

            for itr in range(0, 4):
                new_row = curr_row + row_delta[itr]
                new_col = curr_col + col_delta[itr]

                if new_row >= 0 and new_row < nrows and new_col >= 0 and new_col < ncols and board[new_row][new_col] == "O" and (new_row,new_col) not in visited:
                    dfs(new_row, new_col)
        

        for col in range(ncols):
            if board[0][col] == "O":
                dfs(0, col)
        for row in range(1, nrows):
            if board[row][0] == "O":
                dfs(row, 0)
        for col in range(1, ncols):
            if board[nrows-1][col] == "O":
                dfs(nrows-1, col)
        for row in range(1, nrows-1):
            if board[row][ncols-1] == "O":
                dfs(row, ncols-1)
        
        for row in range(nrows):
            for col in range(ncols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "SS":
                    board[row][col] = "O"

        return

