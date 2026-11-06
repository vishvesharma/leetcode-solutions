class Solution:
    def validPath(self, n, edges, source, destination):
        graph = [[] for i in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        stack = [source]
        seen = set()

        while stack:
            x = stack.pop()
            if x == destination:
                return True
            if x not in seen:
                seen.add(x)
                stack += graph[x]

        return False