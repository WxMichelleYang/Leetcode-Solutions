# Part 1: 
# Given an array of heights (a line of people), how many people can the last person in line see? Rule: person A can see person B if no one standing between them is taller than both A and B. 
# Ex: [1 10 6 7 9 8 2 4 3 5] -> return 6 people (5 can see 3, 4, 2, 8, 9, 10)

# Part 2:
# Same array, but now find, for every person in the line, how many people they can see.

from typing import List
class Solution:
    def solve(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ret = [0] * n
        stack = []
        for i in range(n):
            while len(stack) > 0 and heights[stack[-1]] < heights[i]:
                stack.pop()

            if len(stack) == 0:
                ret[i] = i 
            else:
                ret[i] = len(stack) + i-stack[-1]-1
            stack.append(i)
        return ret
        


test_heights = [1, 10, 6, 7, 9, 8, 2, 4, 3, 5]
s = Solution()
result  = s.solve(test_heights)
print(test_heights)
print(result)