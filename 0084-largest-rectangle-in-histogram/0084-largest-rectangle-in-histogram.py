
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0

        for i in range(len(heights) + 1):

            curr = heights[i] if i < len(heights) else 0

            while stack and heights[stack[-1]] > curr:

                h = heights[stack.pop()]

                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i

                max_area = max(max_area, h * w)

            stack.append(i)

        return max_area
