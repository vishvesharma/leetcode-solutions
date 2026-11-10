
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] == 0:
                return 0

            grid[r][c] = 0  # Mark visited
            return (1 + dfs(r+1, c) + dfs(r-1, c)
                    + dfs(r, c+1) + dfs(r, c-1))

        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    ans = max(ans, dfs(r, c))  # Max area
        return ans
