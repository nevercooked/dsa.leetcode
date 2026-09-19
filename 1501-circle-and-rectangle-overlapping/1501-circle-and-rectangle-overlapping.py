class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        cx = min(x2, max(xCenter, x1))
        cy = min(y2, max(yCenter, y1))
        return (((cx - xCenter)**2 + (cy - yCenter)**2)**0.5) <= radius

        