# 0417 - Pacific Atlantic Water Flow

'''
    Question:
        There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
        The island is partitioned into a grid of square cells. 
        You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
        The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
        Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        '''
            Method: 
                The scan of the matrix starts from the edge of the matrix, as the dfs algorithm climbing the slope of the island, 
                we can obtain the path to reach the highest point from the edge of the matrix.
        '''

        self.heights = heights              # Initialization
        self.rows, self.cols = len(heights), len(heights[0])
        self.pacific_traversed = set()      # The traversal of the pacific starts from the left and top edge of the matrix. 
        self.atlantic_traversed = set()     # The traversal of the pacific starts from the right and bottom edge of the matrix.
        self.directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for row in range(self.rows):
            self.dfs(self.pacific_traversed, row, 0)
            self.dfs(self.atlantic_traversed, row, self.cols - 1)
        for col in range(self.cols):
            self.dfs(self.pacific_traversed, 0, col)
            self.dfs(self.atlantic_traversed, self.rows - 1, col)
    
        return list(self.pacific_traversed & self.atlantic_traversed) 
        # By doing AND operation we can obtain the points that can reach both Pacific & Atlantic Ocean.

    def dfs(self, traversed, i, j):
        if (i, j) in traversed:
            return
        traversed.add((i, j))

        for direction in self.directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if self.rows > next_i >= 0 and self.cols > next_j >= 0:
                if self.heights[next_i][next_j] >= self.heights[i][j]:
                    self.dfs(traversed, next_i, next_j)        

if __name__ == '__main__':
    heights =   [
                    [1,2,2,3,5],
                    [3,2,3,4,4],
                    [2,4,5,3,1],
                    [6,7,1,4,5],
                    [5,1,1,2,4],
                ]
    sol = Solution()
    ans = sol.pacificAtlantic(heights)
    print(ans)