class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0
        for i, ch in enumerate(s):
            degree += ((i + 1) * (26 - (ord(ch) - ord('a'))))
        return degree