# # solution 1 O(n^2)
# class Solution:
#     def findMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         maxLen = 0
#         lCountZeros = [0 for _ in range(n)]
#         lCountZeros[0] = 1 if nums[0] == 0 else 0
#         for i in range(1, n):
#             if nums[i] == 0:
#                 lCountZeros[i] = lCountZeros[i-1] + 1
#             else:
#                 lCountZeros[i] = lCountZeros[i-1]
                
#         for i in range(0, n):
#             for j in range(i+1, n):
#                 countZero = lCountZeros[j] 
#                 if i > 0:
#                     countZero -= lCountZeros[i-1]
#                 countOne = j-i+1 - countZero
                
#                 if countZero == countOne:
#                     curLen = j - i + 1
#                     maxLen = max(curLen, maxLen)
#         return maxLen

# Solution 2 O(n)
# for a sub arry nums[:i], if there is a prefix sub array nums[:j], where j<i
# and their imbalance are the same: zeros[i] - ones[i] == zeros[j] - ones[j],
# the subarray nums[j+1:i] is balanced 
# and since ones[i] = i+1 - zeros[i]
# so the imbalance between 0s and 1s can be represented as:
# zeros[i] - (i+1) + zeros[i] = 2*zeros[i] - (i+1)
# using this formula can make the time complexity collapses to O(n)

from collections import defaultdict
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxLen = 0
        lCountZeros = [0 for _ in range(n)]
        lCountZeros[0] = 1 if nums[0] == 0 else 0
        for i in range(1, n):
            if nums[i] == 0:
                lCountZeros[i] = lCountZeros[i-1] + 1
            else:
                lCountZeros[i] = lCountZeros[i-1]

        valIndex = defaultdict()
        for i in range(0, n):
            curVal = 2*lCountZeros[i] - i
            if (2*lCountZeros[i]) == (i+1):
                curLen = i+1
                maxLen = max(maxLen, curLen)
                if curVal not in valIndex:
                    valIndex[curVal] = i
                continue
            if curVal in valIndex:
                j = valIndex[curVal]
                curLen = i - j 
                maxLen = max(maxLen, curLen)
            else:
                valIndex[curVal] = i

        return maxLen