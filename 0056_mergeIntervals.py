# 0056 - Merge Intervals

'''
    Question:
        Given an array of intervals where intervals[i] = [starti, endi],
        merge all overlapping intervals, and return an array of the non-overlapping
        intervals that cover all the intervals in the input.
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # Solution 1
        out = []
        for i in sorted(intervals):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out.append(i)
        return out
    
        # # Solution 2
        # intervals.sort()
        # i = 1
        # while i < len(intervals):
        #     if intervals[i][0] <= intervals[i - 1][1]:
        #         intervals[i] = [intervals[i - 1][0], max(intervals[i][1], intervals[i - 1][1])]
        #         del intervals[i - 1]
        #     else:
        #         i += 1
        # return intervals

if __name__ == '__main__':
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals = [[1,4],[1,4]]
    sol = Solution()
    print(sol.merge(intervals))