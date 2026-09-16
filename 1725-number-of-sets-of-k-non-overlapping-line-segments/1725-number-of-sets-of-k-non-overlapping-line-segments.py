class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod  = 10**9 + 7 
        dp   = [[0] * n for _ in range(k + 1)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, k + 1):
            prefix = 0
            for j in range(1, n):
                prefix   += dp[i - 1][j - 1]
                prefix   %= mod
                dp[i][j]  = dp[i][j - 1] + prefix
                dp[i][j] %= mod
        return dp[k][n - 1]