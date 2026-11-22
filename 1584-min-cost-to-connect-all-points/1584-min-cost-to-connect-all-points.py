
class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)

        visited = [False] * n
        min_cost = [float('inf')] * n

        min_cost[0] = 0
        total = 0

        for i in range(n):
            smallest = float('inf')
            current = -1

            for j in range(n):
                if visited[j] == False and min_cost[j] < smallest:
                    smallest = min_cost[j]
                    current = j

            visited[current] = True
            total += smallest

            for j in range(n):
                if visited[j] == False:
                    x1 = points[current][0]
                    y1 = points[current][1]

                    x2 = points[j][0]
                    y2 = points[j][1]

                    distance = abs(x1 - x2) + abs(y1 - y2)

                    if distance < min_cost[j]:
                        min_cost[j] = distance

        return total
