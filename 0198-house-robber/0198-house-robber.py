class Solution:
    def rob(self, nums: list[int]) -> int:
        a = 0
        b = 0

        for money in nums:
            c = max(a + money, b)  # Rob ya skip
            a = b
            b = c

        return b