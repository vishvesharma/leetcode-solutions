
class Solution:
    def orangesRotting(self, grid):
        from collections import deque

        q = deque()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                for x, y in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + x, c + y

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                        if grid[nr][nc] == 1:
                            grid[nr][nc] = 2  # Rot orange
                            fresh -= 1
                            q.append((nr, nc))

            minutes += 1  # Next minute

        if fresh > 0:
            return -1
        return minutes
