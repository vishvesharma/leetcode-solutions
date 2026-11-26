class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:

        m = len(students)
        n = len(students[0])

        score = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                for q in range(n):
                    if students[i][q] == mentors[j][q]:
                        score[i][j] += 1

        dp = [-1] * (1 << m)
        dp[0] = 0

        for mask in range(1 << m):

            student = bin(mask).count('1')

            if student == m:
                continue

            for j in range(m):

                if not (mask & (1 << j)):

                    new_mask = mask | (1 << j)

                    dp[new_mask] = max(
                        dp[new_mask],
                        dp[mask] + score[student][j]
                    )

        return dp[(1 << m) - 1]