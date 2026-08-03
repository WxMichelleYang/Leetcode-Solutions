class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        q = deque() # (i, prefixSum) 
        prefixSum = 0
        shortest = len(nums) + 1
        for i, num in enumerate(nums):
            prefixSum += num
            if prefixSum >= k:
                shortest = min(shortest, i+1)
            while q and prefixSum-q[0][1] >= k:
                node = q.popleft()
                shortest = min(shortest, i-node[0])
            while len(q) > 0 and q[-1][1] >= prefixSum:
                q.pop()
            q.append((i, prefixSum))
            # print(i,q,shortest)
        if shortest == len(nums)+1:
            return -1
        return shortest

# for line 10, I have tried to scan the array from tail to head, the worst time complexity is O(n^2)
# So if scanning from head to tail, if a subarray is found, we can remove the head forever, and it can optimize the time complexity to O(n)