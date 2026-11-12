class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        nrows = len(board)
        ncols = len(board[0])  
        dx = [0,-1,1,0]
        dy = [-1,0,0,1]   
        n = len(word)

        def dfs(row, col, idx, visited):

            if idx >= n-1:
                return True

            visited.add((row, col))

            for itr in range(4):
                nx = row + dx[itr]
                ny = col + dy[itr]
                if 0<=nx<nrows and 0<=ny<ncols and (nx, ny) not in visited and idx+1 < n and board[nx][ny] == word[idx+1]:
                    if dfs(nx, ny, idx+1, visited):
                        return True
            visited.remove((row, col))
            return False

        for i in range(nrows):
            for j in range(ncols):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i, j, 0, visited):
                        return True
                    
                    
        return False
