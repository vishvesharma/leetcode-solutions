
class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        state = [0] * n

        def dfs(node):
            if state[node] != 0:
                return state[node] == 2

            state[node] = 1  # Visiting

            for next_node in graph[node]:
                if not dfs(next_node):
                    return False

            state[node] = 2  # Safe
            return True

        ans = []
        for i in range(n):
            if dfs(i):
                ans.append(i)

        return ans
