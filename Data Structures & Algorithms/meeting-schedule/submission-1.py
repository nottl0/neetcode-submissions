"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev_y = 0
        intervals = sorted(intervals, key = lambda x: x.start)
        for inter in intervals:
            if inter.start < prev_y:
                return False
            prev_y = inter.end
        return True