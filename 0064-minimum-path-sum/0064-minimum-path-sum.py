class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                if i == 0:
                    grid[i][j] += grid[i][j-1]  # Left se
                elif j == 0:
                    grid[i][j] += grid[i-1][j]  # Upar se
                else:
                    # Chhota path choose kara
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]