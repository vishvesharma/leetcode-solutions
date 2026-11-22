class Solution:
    def networkDelayTime(self, times, n, k):
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        visited = [False] * (n + 1)

        for i in range(n):
            node = -1
            smallest = float('inf')

            for j in range(1, n + 1):
                if not visited[j] and dist[j] < smallest:
                    smallest = dist[j]
                    node = j

            if node == -1:
                break

            visited[node] = True

            for u, v, w in times:
                if u == node:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

        answer = max(dist[1:])

        if answer == float('inf'):
            return -1

        return answer
