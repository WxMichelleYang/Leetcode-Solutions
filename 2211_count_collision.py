# class Solution:
#     def countCollisions(self, directions: str) -> int:
#         n = len(directions)
#         collisions = 0
#         statusStack = []

#         i = 0
#         currentDirection = directions[i]
#         while currentDirection:
#             if currentDirection == 'R':
#                 statusStack.append(currentDirection)
#                 i += 1
#                 if i < n: 
#                     currentDirection = directions[i]
#                 else:
#                     currentDirection = None
#             elif currentDirection == 'L':
#                 if statusStack:
#                     prev = statusStack.pop()
#                     if prev == 'S':
#                         collisions += 1
#                         currentDirection = 'S'
#                         continue
#                     elif prev == 'R':
#                         collisions += 2
#                         currentDirection = 'S'
#                         continue
#                 statusStack.append(currentDirection)
#                 i += 1
#                 if i < n: 
#                     currentDirection = directions[i]
#                 else:
#                     currentDirection = None
#             else: # current direction == 'S'
#                 while statusStack and statusStack[-1] == 'R':
#                     collisions += 1
#                     statusStack.pop()
#                 statusStack.append(currentDirection)
#                 i += 1
#                 if i < n:
#                     currentDirection = directions[i]
#                 else:
#                     currentDirection = None
#         return collisions
# 
# Since except leading L and tailing R, all other cars will finally stop either by 
# colliding with a stopped car or a moving car, and if they are moving cars, i.e. RL,
# the collision is 2, and if is RS or SL, the collision is 1, so the total number 
#  of collision is the number of Ls and Rs after removing leading Ls and trailing Rs
# Solution 2
class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        collisions = 0
        i = 0
        while i < n and directions[i] == 'L':
            i += 1
        j = n-1
        while j>=0 and directions[j] == 'R':
            j -= 1
        while i <= j:
            if directions[i] != 'S':
               collisions += 1
            i += 1 
        return collisions
            