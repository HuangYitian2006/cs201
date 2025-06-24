class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        c, r = len(board[0]), len(board)
        flag = False
        def dfs(ind, x, y):
            if flag: return
            if ind == len(word):
                flag = True
                return
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == word[ind]:
                    dfs(ind + 1, nx, ny)

        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    dfs(1, i, j)
        return flag
