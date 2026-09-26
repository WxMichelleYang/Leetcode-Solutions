# from typing import List
# from sortedcontainers import SortedDict
# class Solution:
#     def SlidingWindowAverage(self, nums: List[int], windowSize: int, k: int) -> List[float]:
#         # TODO: Implement SlidingWindowAverage logic
#         ret = []
#         l = 0
#         r = 0
        
#         topkNums = SortedDict()
#         restNums = SortedDict()
#         topksize = 0
#         windowSum = 0
#         topkSum = 0
#         n = len(nums)
#         while r < n:
#             while (r-l+1) <= windowSize:
#                 val = nums[r]
#                 r += 1
#                 windowSum += val
#                 topkNums[val] = topkNums.get(val, 0) + 1
#                 topkSum += val
#                 topksize += 1
#                 if topksize > k:
#                     smallest = topkNums.peekitem(0)[0]
#                     topkNums[smallest] -= 1
#                     if topkNums[smallest] == 0:
#                         del topkNums[smallest]
#                     topksize -= 1
#                     topkSum -= smallest
#                     restNums[smallest] = restNums.get(smallest,0) + 1
            
#             avg = (windowSum - topkSum)/(windowSize - k)
#             ret.append(avg)

#             val = nums[l]
#             l += 1
#             windowSum -= val
#             if val in topkNums:
#                 topkNums[val] -= 1
#                 topksize -= 1
#                 topkSum -= val
#                 if topkNums[val] == 0:
#                     del topkNums[val]
#                 largest = restNums.peekitem(-1)[0]
#                 topkNums[largest] = topkNums.get(largest,0) + 1
#                 topksize += 1
#                 topkSum += largest
#                 restNums[largest] -= 1
#                 if restNums[largest] == 0:
#                     del restNums[largest]
#             else:
#                 restNums[val] -= 1
#                 if restNums[val] == 0:
#                     del restNums[val]
#         return ret

# A more nit solution:
# 1. two sets topkNums and restNums
# 2. sliding window, for a new element: add to restNums -> select the largest element in restNums and insert to topKNums
#     -> if the size of topKNums > k, pop the smallest num in topKNums and insert to restNums, to always maintain topKNums;


from typing import List, Optional
from sortedcontainers import SortedDict

class MySortedDict:
    def __init__(self):
        self.valFreq = SortedDict()
        self.size = 0
        self.sum = 0
    
    def hasVal(self, val):
        return val in self.valFreq
    
    def add(self, val:int):
        self.valFreq[val] = self.valFreq.get(val, 0) + 1
        self.size += 1
        self.sum += val
    
    def pop(self, val:int):
        if val not in self.valFreq:
            return
        self.valFreq[val] -= 1
        if self.valFreq[val] == 0:
            del self.valFreq[val]
        self.size -= 1
        self.sum -= val
    
    def popLargest(self):
        largest = self.valFreq.peekitem(-1)[0]
        self.pop(largest)
        return largest
    
    def popSmallest(self):
        smallest = self.valFreq.peekitem(0)[0]
        self.pop(smallest)
        return smallest
    
class Solution:
    def SlidingWindowAverage(self, nums: List[int], windowSize: int, k: int) -> List[float]:
        # TODO: Implement SlidingWindowAverage logic
        ret = []
        l = 0
        r = 0
        
        topkNums = MySortedDict()
        restNums = MySortedDict()
        windowSum = 0
        n = len(nums)
        while r < n:
            while (r-l+1) <= windowSize:
                val = nums[r]
                r += 1
                windowSum += val
                restNums.add(val)
                topkNums.add(restNums.popLargest())
                if topkNums.size > k:
                    restNums.add(topkNums.popSmallest())
            
            avg = (windowSum - topkNums.sum)/(windowSize - k)
            ret.append(avg)

            val = nums[l]
            l += 1
            windowSum -= val
            if restNums.hasVal(val):
                restNums.pop(val)
            else:
                topkNums.pop(val)  
        return ret
                