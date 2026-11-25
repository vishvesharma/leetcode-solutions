class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)

        dp = {0: 0}

        for i in range(n):

            new_dp = {}

            for mask in dp:

                for j in range(n):

                    if (mask & (1 << j)) == 0:

                        new_mask = mask | (1 << j)

                        cost = nums1[i] ^ nums2[j]

                        value = dp[mask] + cost

                        if new_mask not in new_dp or value < new_dp[new_mask]:
                            new_dp[new_mask] = value

            dp = new_dp

        return dp[(1 << n) - 1]