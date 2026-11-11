class Solution:
    def findRedundantConnection(self, edges):
        parent = list(range(len(edges) + 1))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for a, b in edges:
            x = find(a)
            y = find(b)

            if x == y:
                return [a, b]  # Cycle found

            parent[x] = y  # Connect nodes
