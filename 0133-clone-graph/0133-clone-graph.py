
class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        def dfs(old):
            if old in visited:
                return visited[old]

            new = Node(old.val)  # Copy node
            visited[old] = new

            for neighbor in old.neighbors:
                new.neighbors.append(dfs(neighbor))  # Copy links

            return new

        return dfs(node)
