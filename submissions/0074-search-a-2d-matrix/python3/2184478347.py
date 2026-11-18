class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rmax = len(matrix)
        cmax = len(matrix[0])

        lo = 0
        hi = (rmax * cmax) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            
            r = mid // cmax
            c = mid % cmax
            
            val = matrix[r][c]

            if val == target:
                return True
            elif val < target:
                lo = mid + 1
            else:
                hi = mid - 1
                
        return False