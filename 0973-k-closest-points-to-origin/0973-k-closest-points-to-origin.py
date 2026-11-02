class Solution:
    def kClosest(self, points, k):
        distances = []

        for p in points:
            x = p[0]
            y = p[1]

            d = x*x + y*y  # Distance nikala
            distances.append([d, p])

        distances.sort()  # Choti distance pehle

        ans = []

        for i in range(k):
            ans.append(distances[i][1])

        return ans
    