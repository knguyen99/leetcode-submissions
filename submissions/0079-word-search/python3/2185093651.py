class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        dirs = ((1,0), (0,1), (-1, 0), (0, -1) )
        
        def valid(x,y):
            return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != None
        
        def helper(x,y,i):
            if i == len(word):
                return True
            if not valid(x,y):
                return False
            if board[x][y] != word[i]:
                return False
            save = board[x][y]
            board[x][y] = None
            for dx, dy in dirs:
                newx, newy = x + dx, y + dy
                if helper(newx,newy,i + 1):
                    return True
            board[x][y] = save
            return False
        
        for x in range(len(board)):
            for y in range(len(board[0])):
                if helper(x,y,0):
                    return True
        return False
            