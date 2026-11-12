class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        nrows = len(board)
        ncols = len(board[0])        
        n = len(word)
        dx = [0,-1,1,0]
        dy = [-1,0,0,1]
        

        def helper(i, j, idx, visited):
            print(i, j)
            if idx >= n-1:
                return True
            
            visited[i][j] = True

            for itr in range(4):
                nx = i + dx[itr]
                ny = j + dy[itr]
                if 0<=nx<nrows and 0<=ny<ncols and not visited[nx][ny] and board[nx][ny]==word[idx+1]:
                    if helper(nx, ny, idx+1, visited):
                        return True
            visited[i][j] = False
            return False


        for i in range(nrows):
            for j in range(ncols):
                if board[i][j] == word[0]:
                    visited = [[0] * ncols for _ in range(nrows)]
                    if helper(i, j, 0, visited):
                        return True
                    
    
        return False

