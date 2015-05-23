# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    # leetcode 56 Merge Intervals 
    # scarlett Chen
    # 5/23/2015 sat 6:35 pm
    # 思路很简单，写法可借鉴。先排序：java可以用collections.sort( new comparator()); python 可以用(key = lambda x:...)
    # 比较两者的start, 前者的end和后者的start,两者的end .结果可得。
    def merge(self, intervals):
        if len(intervals)<=1:
            return intervals
        intervals = sorted(intervals, key = lambda x:x.start)
        result = []
        result.append(intervals[0])
        for interval in intervals:
            if interval.start > result[-1].end:
                result.append(interval)
            elif interval.end > result[-1].end:
                result[-1].end = interval.end
        return result
        
