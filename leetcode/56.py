'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

'''


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res=[]
        intervals.sort(key=lambda x:x.start)
        if not intervals:
            return []
        start=intervals[0].start
        end=intervals[0].end
        for interval in intervals:
            if interval.start > end:
                res.append(Interval(start, end))
                start=interval.start
                end=interval.end
                for i in res:
                    print(i.start, i.end)
            elif interval.end<=end:
                continue
            else:
                end=interval.end
        res.append(Interval(start,end))
        return res

a=Interval(1,3)
b=Interval(2,6)
c=Interval(8,10)
d=Interval(15,18)
l=[a,b,c,d]

s=Solution()
s.merge(l)