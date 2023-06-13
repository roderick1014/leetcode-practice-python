# 0452 - Minimum Number of Arrows to Burst Balloons

'''
    Question:
        There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
        The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] 
        denotes a balloon whose horizontal diameter stretches between xstart and xend. 
        
        You do not know the exact y-coordinates of the balloons.

        Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
        A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. 
        There is no limit to the number of arrows that can be shot. 
        A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

        Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
        There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
        The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a 
        balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

        Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. 
        A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. 
        There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

        Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
'''


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        '''
            Idea: 
                1. Sort the array by end (Ex: [[1,3],[1,2],[3,9], [2,6]] -> [[1,2],[1,3],[2,6],[3,9]])
                2. Put an arrow at the end of a segment Ex: 3 of segment [1, 3]
                3. Traverse each segment and check if there's any start of a segment is larger than the arrow we point to.
                4. If there's a segment that is larger than the arrow we point to, update the arrow to the end of that segment.
            
            ========================================================================================================================
            
            Where we currently point to.
                          |
                __________v
                    ___________             New arrow as we found there's a new start point that's larger than previous end point.
                  __________                           |
                                        _______________v
                                              _________
            
            ========================================================================================================================
        '''
        
        points.sort(key=lambda arr: arr[1]) # Sorted by the end
        shoot = 0 
        arrow = float('-inf')

        for point in points:
            if point[0] > arrow:
                shoot += 1
                arrow = point[1]
        return shoot

if __name__ == '__main__':
    # points = [[10,16],[2,8],[1,6],[7,12]]
    # points = [[1,2],[3,4],[5,6],[7,8]]
    # points = [[1,2],[2,3],[3,4],[4,5]]
    points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
    sol = Solution()
    print(sol.findMinArrowShots(points))