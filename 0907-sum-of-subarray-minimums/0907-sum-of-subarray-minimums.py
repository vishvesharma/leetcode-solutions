class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:

        n = len(arr)
        stack = []
        answer = 0

        for i in range(n + 1):

            while stack and (i == n or arr[stack[-1]] > arr[i]):

                mid = stack.pop()

                if stack:
                    left = stack[-1]
                else:
                    left = -1

                right = i

                left_count = mid - left
                right_count = right - mid

                answer += arr[mid] * left_count * right_count

            stack.append(i)

        return answer % (10**9 + 7)