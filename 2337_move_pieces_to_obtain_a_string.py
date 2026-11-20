# Solution 1
# class Solution:        
#     def canChange(self, start: str, target: str) -> bool:
#         n = len(start)
#         lMove = [n] * n
#         leftMost = 0
#         for i in range(n):
#             if start[i] == 'L':
#                 lMove[i] = leftMost
#                 leftMost += 1
#             elif start[i] == 'R':
#                 leftMost = i + 1
#         rightMost = n-1
#         rMove = [-1] * n
#         for i in range(n-1, -1, -1):
#             if start[i] == 'R':
#                 rMove[i] = rightMost
#                 rightMost -= 1
#             elif start[i] == 'L':
#                 rightMost = i - 1

#         si = 0
#         ti = 0
#         while ti < n and si < n:
#             if target[ti] == 'L':
#                 while si < n and start[si] == '_':
#                     si += 1
#                 if si == n or start[si] != 'L':
#                     return False
#                 if ti < lMove[si] or ti > si:
#                     return False 
#                 si += 1   
#             elif target[ti] == 'R':
#                 while si < n and start[si] == '_':
#                     si += 1
#                 if si == n or start[si] != 'R':
#                     return False
#                 if ti > rMove[si] or ti < si:
#                     return False
#                 si += 1
#             ti += 1

#         if ti < n:
#             while ti < n and target[ti] == '_':
#                 ti += 1
#             if ti < n:
#                 return False
        
#         while si < n and start[si] == '_':
#             si += 1
#         if si < n:
#             return False

#         return True


# Solution 2
class Solution:        
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        si = 0
        ti = 0
        while ti < n or si < n:
            while ti < n and target[ti] == '_':
                ti += 1
            
            while si < n and start[si] == '_':
                si += 1
            
            if ti == n:
                return si == n
            
            if si == n:
                return False

            if target[ti] != start[si]:
                return False
            
            if target[ti] == 'L':
                if ti > si:
                    return False
            else:
                if ti < si:
                    return False
            ti += 1
            si += 1

        return True