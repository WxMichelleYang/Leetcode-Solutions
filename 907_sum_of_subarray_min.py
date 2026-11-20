# class Solution:
#     def sumSubarrayMins(self, arr: list[int]) -> int:
#         n = len(arr)
#         winMin = [[0] * n for _ in range(n)]
#         sum = 0
#         for i in range(n):
#             winMin[i][i] = arr[i]
#             sum = (sum + winMin[i][i]) % (1000000007)
#         for l in range(2, n+1, 1):
#             i = 0
#             while ((i + l - 1) < n):
#                 j = i+l-1
#                 winMin[i][j] = min(winMin[i][j-1], arr[j])
#                 sum = (sum + winMin[i][j]) % 1000000007
#                 i += 1
            
#         return sum

# Solution 2
# for every arr[i] we can try to calculate how many sub arrays it is as the min value;
# so we only need to determine the sub array's left bound and right bound; 
# the left bound is the first arr[j] < arr[i] and j<i
# and the right bound is the first arr[k] < arr[i] where k>i
# and the number of subarrays is (i-j)*(k-i)
# So my method is to use a deque to maintain the min values;


from collections import deque
class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n = len(arr)
        count = [0] * n
        q = deque()
        for i in range(n):
            if q:
                while q and arr[q[-1]] >= arr[i]:
                    count[q[-1]] *= i-q[-1]
                    q.pop()
            if not q:
                count[i] = i + 1
            else:
                count[i] = i - q[-1]
            q.append(i)
        
        while q:
            i = q.popleft()
            count[i] *= n-i
            
        ret = 0
        for i in range(n) :
            val = (count[i]%1000000007) * (arr[i]%1000000007)
            ret += val
            ret = ret % 1000000007
        return ret