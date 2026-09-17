class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n  = len(arr)
        s  = 0
        i  = 0
        dp = [+inf] * (n + 1)
        min_len = +inf
        for j, num in enumerate(arr):
            s += num
            while i <= j and s > target:
                s -= arr[i]
                i += 1
            if s == target:
                curr_len  = j - i + 1
                min_len   = min(min_len, dp[i] + curr_len)
                dp[j + 1] = min(dp[j], curr_len)
            else:
                dp[j + 1] = dp[j]
        return -1 if min_len == +inf else min_len