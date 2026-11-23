
import heapq

class Solution:
    def minimumEffortPath(self, heights):
        rows = len(heights)
        cols = len(heights[0])

        dist = [[float('inf')] * cols for i in range(rows)]
        dist[0][0] = 0

        heap = [(0, 0, 0)]

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while heap:
            effort, x, y = heapq.heappop(heap)

            if x == rows - 1 and y == cols - 1:
                return effort

            if effort > dist[x][y]:
                continue

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    difference = abs(heights[x][y] - heights[nx][ny])

                    new_effort = max(effort, difference)

                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heapq.heappush(heap, (new_effort, nx, ny))

        return 0
