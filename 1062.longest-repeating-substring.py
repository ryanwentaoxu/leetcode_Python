class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(s) + 1)]
        ans = 0
        for i in range(1, len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                if (s[i - 1] == s[j - 1]):
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans