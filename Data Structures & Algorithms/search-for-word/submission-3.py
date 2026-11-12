class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])  
        dx = [0, -1, 1, 0]
        dy = [-1, 0, 0, 1]
        visited = [[False] * n for _ in range(m)]

        def helper(i, j, idx, status):
            if idx == len(word)-1:
                return True

            for itr in range(4):
                nx = i + dx[itr]
                ny = j + dy[itr]
                if 0 <= nx < m and 0 <= ny < n and not status[nx][ny] and (idx+1) < len(word) and board[nx][ny] == word[idx+1]:
                    print(nx, ny, idx)
                    status[nx][ny] = True
                    if helper(nx, ny, idx+1, status):
                        return True
                    status[nx][ny] = False
            return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if helper(i, j, 0, visited):
                        return True
                    visited[i][j] = False
        return False