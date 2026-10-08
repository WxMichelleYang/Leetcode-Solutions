# Solution 1
# The brute force method is to check whether target is a majority element 
# for every subarray nums[i:j]
# Give a subarray, nums[i:j]:
# Accoring to the definition of majority element is the number of an element is 
# larger than l/2, which mean more than half of the elements are target;
# so we can use a formular: 
# dp[i][j] = sum(1 if nums[k] == target else -1) (k=i...j)
# dp[i][j] is the imbalance between majority elements and other elements;
# since there are n^2 subarrays, and the time required to process every 
# subarray will also be O(n), the time complexity of this brute force 
# solution is O(n^3) 
# and since dp[i][j] = dp[i][j-1] + (1 if nums[j] == target else -1)
# The time complexity can be O(n^2)
# The space complexity is also O(n^2)

# class Solution:
#     def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         dp = [[0 for _ in range(n)] for _ in range(n)] 
        
#         count = 0
#         for i in range(n):
#             for j in range(i, n):
#                 num = nums[j]
#                 if j == i:
#                     dp[i][j] = 1 if num == target else -1
#                 else:
#                     dp[i][j] = dp[i][j-1] + (1 if num == target else -1)
#                 if dp[i][j] >= 1:
#                     count += 1
        
#         return count

# Solution 2
# In the above solution 1, We noticed that every dp[i][j] only relies on 
# dp[i][j-1], it means we can use a 1D array, e.g. dp[j] to record the   
# imbalance of majority elements in nums[:j], and using dp[j] - dp[i] to 
# calculate the imbalance  in nums[i:j], and if dp[j] - dp[i] is > 0,
# target is a majority element in nums[i:j], therefore, we can keep dp[i] sorted,
# and given a new dp[i+1], we only need to check how many values in dp[:i] 
# is smaller than dp[i+1], that's the number of sub arrays where target
# is a majority number. For every dp[i+1], the number can be calculated 
# using binary search in O(logn) time complexity. But the time complexity of inserting
# dp[i+1] to dp[:i] is also O(n), so the overall time complexity is still O(n^2)
# but space complexity is O(n) 

import bisect
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        prefix = [0]
        prev = 0

        for i in range(1, n+1):
            prev = prev + (1 if nums[i-1] == target else -1)
            count += bisect.bisect_left(prefix, prev)
            bisect.insort_left(prefix, prev)
        
        return count

