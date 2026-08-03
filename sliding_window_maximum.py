from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxStack = deque()
        ret = []
        start = 0
        i = 0
        l = len(nums)
        while(i < l):
            while((i-start) < k) and i < l:
                while len(maxStack) > 0 and maxStack[-1] < nums[i]:
                    maxStack.pop()
                maxStack.append(nums[i])
                i += 1
            ret.append(maxStack[0])
            if nums[start] == maxStack[0]:
                maxStack.popleft()
            start += 1
        return ret


# Used deque to track all the possible max numbers, 