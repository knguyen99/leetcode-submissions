class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 2 alive -> dead
        # -1 dead -> alive

        def calculate(i,j):
            count = 0
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if dx == dy == 0:
                        continue
                    newi, newj = i + dx, j + dy
                    if 0 <= newi < len(board) and 0 <= newj < len(board[0]) and board[newi][newj] > 0:
                        count += 1
            if board[i][j] == 1 and (count < 2 or count > 3) :
                return 2
            elif board[i][j] == 0 and count == 3:
                return -1
            return board[i][j]

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = calculate(i,j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                elif board[i][j] == -1:
                    board[i][j] = 1