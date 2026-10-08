# You are given a list of trees, where trees[i] = [xi, yi] is the position of the i-th tree in a forest. No tree is at the origin.

#   You have cameras that can only be placed at the origin (0, 0). Each camera has a fixed field of view of fov degrees. A camera placed at angle d captures every tree whose angle lies in the closed arc [d,
#   d + fov], measured counter-clockwise and taken modulo 360.

#   You are given a predefined API:

#   # Definition of the provided API.
#   # def getAngle(x: int, y: int) -> float:
#   #     """Returns the angle in degrees that (x, y) makes with the positive
#   #        x-axis, measured counter-clockwise. The result is in [0, 360).
#   #        You should not implement it or speculate about its implementation."""

#   Return a list of camera angles of minimum possible size such that every tree is captured by at least one camera.

#   Each returned angle must be equal to getAngle(xi, yi) for some tree i. If several answers of minimum size exist, return any of them, in any order.

#   Example 1

#   Input:  trees = [[1,0],[2,1],[3,1]], fov = 90
#   Output: [0]
#   The three trees sit at 0°, 26.565°, and 18.435°. One camera placed at 0 covers the arc [0, 90], which contains all three.

#   Example 2

#   Input:  trees = [[1,1],[1,-1]], fov = 90
#   Output: [315]
#   The trees sit at 45° and 315°. A camera at 315 covers [315, 405], and 405 mod 360 = 45, so it wraps past the positive x-axis and catches both. A camera at 45 would cover only [45, 135], missing the
#   other tree — so 315 is the only single-camera answer.

#   Example 3

#   Input:  trees = [[1,0],[0,1],[-1,0],[0,-1]], fov = 90
#   Output: [0,180]
#   Trees sit at 0°, 90°, 180°, 270°. A camera at 0 covers [0, 90], capturing the first two — note the arc is closed, so the tree exactly at 90° counts. A camera at 180 covers [180, 270] for the other two.
#   [90, 270] is also accepted.

#   Example 4

#   Input:  trees = [[1,0],[0,1]], fov = 0
#   Output: [0,90]
#   A camera with zero field of view captures only the single ray it points along.

#   Constraints

#   - 1 <= trees.length <= 10^5
#   - -10^4 <= xi, yi <= 10^4
#   - (xi, yi) != (0, 0)
#   - 0 <= fov <= 360
#   - trees may contain duplicate coordinates.

from typing import List
import math
class Solution:
    def toAngle(self, x: int, y:int) -> float:
        return round(math.degrees(math.atan2(y, x)) % 360, 3)

    # def minCameraAngles(self, trees: List[List[int]], fov: int) -> List[float]:
    #     ret = []
    #     angles = [self.toAngle(tree[0], tree[1]) for tree in trees]
    #     angles.sort()
    #     print(angles)

    #     return ret

    def isCovered(self, angle, start, fov):
        if (angle - start)%360 <= fov :
            return True
        return False


    def cameraPlacement(self, angles: List[float], fov: int, start: int) -> List[float]:
        n = len(angles)

        ret = [angles[start]]
        i = 1
        while i < n:
            j = (start + i)%n
            if not self.isCovered(angles[j], ret[-1], fov):
                ret.append(angles[j])
            
            i += 1
            
        return ret

    def minCameraAngles(self, angles: List[float], fov: int) -> List[float]:
        ret = []
        angles.sort()
        n = len(angles)
        minLen = n + 1
        for start in range(0, n):
            cameraList = self.cameraPlacement(angles, fov, start)

            if len(cameraList) < minLen:
                ret = cameraList
                minLen = len(cameraList)

        return ret

    def covers(self, angles, fov, cameras):
      """Does this camera set actually capture every tree?"""
      return all(any((a - c) % 360 <= fov for c in cameras) for a in angles)

    def reference(self, angles, fov):
        """Smallest valid subset, by exhaustive search. Only for n <= ~12."""
        from itertools import combinations
        uniq = sorted(set(angles))
        for k in range(1, len(uniq) + 1):
            for combo in combinations(uniq, k):
                if self.covers(angles, fov, combo):
                    return list(combo)
        return []

fov: int = 120
# trees = [[1,0],[2,1],[3,1]]
angles = [0, 65, 100, 200, 330, 350]


test = Solution()
cameras = test.minCameraAngles(angles,fov)
test_cameras = test.reference(angles, fov)
print(cameras)
print(test_cameras)