class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n         = len(s)
        start     = [-1] * 26
        end       = [-1] * 26
        intervals = []
        for i, ch in enumerate(s):
            j = ord(ch) - ord('a')
            if start[j] == -1:
                start[j] = i
            end[j] = i
        for i in range(26):
            if start[i] == -1:
                continue
            left  = start[i]
            right = end[i]
            j     = left
            valid = True
            while j <= right:
                k = ord(s[j]) - ord('a')
                if start[k] < left:
                    valid = False
                    break
                right = max(right, end[k])
                j += 1
            if valid:
                intervals.append((left, right))
        intervals.sort(key=lambda p: p[1])
        prev = -1
        strs = []
        for left, right in intervals:
            if prev < left:
                strs.append(s[left:right + 1])
                prev = right
        return strs 