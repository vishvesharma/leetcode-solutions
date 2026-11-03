class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def solve(houses):
            a = 0
            b = 0

            for money in houses:
                c = max(a + money, b)  # Rob ya skip
                a = b
                b = c

            return b

        x = solve(nums[1:])   # First house skip
        y = solve(nums[:-1])  # Last house skip

        return max(x, y)