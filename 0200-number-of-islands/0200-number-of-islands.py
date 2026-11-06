class Solution:
    def numIslands(self, grid):
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            stack = [(i, j)]
            while stack:
                x, y = stack.pop()
                if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                    grid[x][y] = "0"
                    stack += [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count 