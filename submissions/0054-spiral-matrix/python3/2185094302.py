class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        ret = []
        
        dirs = ((0,1), (1,0), (0,-1), (-1,0))
        dir_id = 0
        rmax = len(matrix)
        cmax = len(matrix[0])
        r,c = 0,0
        for _ in range(rmax * cmax):
            if matrix[r][c] == None:
                break
            ret.append(matrix[r][c])
            matrix[r][c] = None

            for _ in range(4):
                dr, dc = dirs[dir_id]
                newr, newc = r + dr, c + dc
                if 0 <= newr < rmax and 0 <= newc < cmax and matrix[newr][newc] != None:
                    r,c = newr, newc
                    break
                dir_id = (dir_id + 1) % 4

        return ret