class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        key = "#"
        for word in words:
            curr = trie
            for letter in word:
                if letter not in curr:
                    curr[letter] = {}
                curr = curr[letter]
            curr[key] = word
        
        rmax = len(board)
        cmax = len(board[0])

        res = []

        dirs = ((1,0), (0,1), (-1,0), (0,-1))

        def search(r,c,parent):
            letter = board[r][c]
            curr = parent[letter]
            
            if key in curr:
                res.append(curr[key])
                curr.pop(key)

            board[r][c] = "*"            
            for dir in dirs:
                newr = dir[0] + r
                newc = dir[1] + c
                if 0 <= newr < rmax and 0 <= newc < cmax and board[newr][newc] in curr:
                    search(newr,newc, curr)

            board[r][c] = letter
        
        for r in range(rmax):
            for c in range(cmax):
                if board[r][c] in trie:
                    search(r,c,trie)
        return res