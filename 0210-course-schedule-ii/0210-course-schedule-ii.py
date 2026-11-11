
class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = [[] for i in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        visited = [0] * numCourses
        ans = []

        def dfs(course):
            if visited[course] == 1:
                return False  # Cycle

            if visited[course] == 2:
                return True

            visited[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            visited[course] = 2
            ans.append(course)  # Add course
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return ans
