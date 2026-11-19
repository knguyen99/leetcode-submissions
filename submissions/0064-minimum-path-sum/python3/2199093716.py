class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dp = [[ float("inf") for _ in range(len(grid[0]))] for _ in range(len(grid))]

        dp[0][0] = grid[0][0]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = min(dp[max(0,i-1)][j], dp[i][max(0,j-1)]) + grid[i][j]
        return dp[-1][-1]