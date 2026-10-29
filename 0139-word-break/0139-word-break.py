class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        words = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True  # Empty string valid

        for i in range(1, n + 1):
            for j in range(i):

                # Pehla part valid ho aur dusra dictionary mein ho
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[n]