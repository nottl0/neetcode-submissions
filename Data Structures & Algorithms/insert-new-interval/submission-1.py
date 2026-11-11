class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s = len(intervals)
        newIntervals = []
        for i in range(s):
            if intervals[i][1] < newInterval[0]:
                newIntervals.append(intervals[i])
                continue

            if intervals[i][0] > newInterval[1]:
                newIntervals.append(newInterval)
                newIntervals.extend(intervals[i:])
                return newIntervals
            else:

                newInterval = [min(intervals[i][0], newInterval[0]),
                                max(intervals[i][1], newInterval[1])]
        newIntervals.append(newInterval)
        return newIntervals