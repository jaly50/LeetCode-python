# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param {Interval[]} intervals
    # @param {Interval} newInterval
    # @return {Interval[]}
    # scarlett Chen
    # 57 leetcode Insert Interval 
    # 5/23/2015 sat 6:43pm  - sat 7:42 pm
    # inplace solution, after reference. It is not easy to retract the main idea
    def insert(self, intervals, newInterval):
        start = newInterval.start
        end = newInterval.end
        left = right =0
        while right <len(intervals):
            if start <= intervals[right].end:
                if intervals[right].start > end:
                    break
                start = min(start, intervals[right].start)
                end = max(end, intervals[right].end)
            else:
                left+=1
            right+=1
        return intervals[:left]+[Interval(start,end)]+intervals[right:]
            
                    
        
