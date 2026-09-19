class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        cx, cy = 0, 0
        if xCenter < x1:
            cx = x1
        elif xCenter > x2:
            cx = x2
        else:
            cx = xCenter
        if yCenter > y2:
            cy = y2
        elif yCenter < y1:
            cy = y1
        else:
            cy = yCenter
        dx   = cx - xCenter
        dy   = cy - yCenter
        dist = (dx**2 + dy**2) ** 0.5
        return dist <= radius

        