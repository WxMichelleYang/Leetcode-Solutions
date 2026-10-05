# Solution 1: O(nlogn)
# class Solution:
#     def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
#         n = len(trips)
#         endPoints = []
#         for trip in trips:
#             endPoints.append((trip[1], trip[0]))
#             endPoints.append((trip[2], -trip[0]))
#         endPoints.sort()
#         count = 0
#         for point in endPoints:
#             count += point[1]
#             if count > capacity:
#                 return False

#         return True

# Solution 2: O(n) optimized by using 1001 buckets, because from, to in [0,1000]
class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        passengers = [0] * 1001
        for trip in trips :
            count = trip[0]
            passengers[trip[1]] += count
            passengers[trip[2]] += -count
        
        sum = 0
        for i in range(0, 1001):
            sum += passengers[i]
            if sum > capacity:
                return False
        return True