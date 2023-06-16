# 0057 - Insert Interval

'''
    Question:
        You are given an array of non-overlapping intervals intervals
        where intervals[i] = [starti, endi] represent the start and the
        end of the ith interval and intervals is sorted in ascending order by starti.

        You are also given an interval newInterval = [start, end] that represents
        the start and end of another interval.

        Insert newInterval into intervals such that intervals is still sorted in ascending
        order by starti and intervals still does not have any overlapping intervals
        (merge overlapping intervals if necessary).

        Return intervals after the insertion.
'''

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        # Solution 2 - Starting & Ending point recording. (Less memory ?)
        if intervals == []:
            return [newInterval]

        start = None
        end = None

        for i in range(len(intervals)):
            currentStart = intervals[i][0]
            currentEnd = intervals[i][1]

            if currentEnd >= newInterval[0] and start == None:      # Check the starting point
                start = i
            if currentStart <= newInterval[1]:                      # Check the ending point
                end = i

        if start == None: return intervals + [newInterval]          # No start means the newInterval is larger than the intervals
        if end == None: return [newInterval] + intervals[start::]   # No end means the newInterval is smaller than the intervals

        result = intervals[:start] + [[min(newInterval[0], intervals[start][0]),max(newInterval[1], intervals[end][1])]] + intervals[end+1::]

        return result

        # # Solution 1 - List recording
        # new_left, new_right = newInterval[0], newInterval[1]
        # left, right = [], []
        # for interval in intervals:
        #     if interval[1] < new_left:      # If the traversed interval is less than the start val of newInterval.
        #         left += interval,           # To replace .append() by "+="", we have to add a ","
        #     elif interval[0] > new_right:   # If the traversed interval is larger than the end val of newInterval.
        #         right += interval,
        #     else:                           # Case if the traversed interval is "in" the range of newInterval.
        #         new_left = min(new_left, interval[0])
        #         new_right = max(new_right, interval[1])
        # return left + [[new_left, new_right]] + right

if __name__ == '__main__':
    intervals = [[1,3], [6,9]]
    newInterval = [2,5]
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    sol = Solution()
    print(sol.insert(intervals, newInterval))