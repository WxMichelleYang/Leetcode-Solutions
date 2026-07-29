class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time_ends = []
        for interval in intervals:
            time_ends.append((interval[0], 0))
            time_ends.append((interval[1], 1))
        time_ends = sorted(time_ends, key = lambda x: (x[0], -x[1]))
        need = 0
        max_need = 0
        for time_end in time_ends:
            if time_end[1] == 0:
                need += 1
            else:
                need -= 1
            if max_need < need:
                max_need = need
        return max_need