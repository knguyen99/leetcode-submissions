class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = ["" for i in range(numRows)]
        
        r = 0
        dir = False
        
        for c in s:
            rows[r] += c
            if r == 0 or r == numRows  - 1: 
                dir = not dir
            if not dir:
                r -= 1
            else:
                r += 1
        return "".join(rows)
            
                