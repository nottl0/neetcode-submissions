class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        newIntervals =[]
        s = len(intervals)
        i = 1
        if s == 1:
            return intervals

        intervals = sorted(intervals, key=lambda s: s[0])
        begin = intervals[0][0]
        end = intervals[0][1]

        while i < s:
            if intervals[i][0] > end:
                newIntervals.append([begin, end])
                begin = intervals[i][0]
                end = intervals[i][1]
            if intervals[i][0] <= end:
                if intervals[i][1] > end:
                    end = intervals[i][1]
            i += 1
        newIntervals.append([begin, end])
        return newIntervals
