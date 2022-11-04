# 0200 - Number of Islands

'''
    Question:
        Given an m x n 2D binary grid 'grid' which represents a map of '1's (land) and '0's (water), return the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
        You may assume all four edges of the grid are all surrounded by water.
'''



class Solution(object):

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # DFS algorithm is needed.

        count_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    count_islands += 1

        return count_islands
    
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != '1': # Stop condition of the dfs algorithm.
            return 
        grid[row][col] = '#' # If the path is traversed, set a flag on it.
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
        
if __name__ == '__main__':
    
    # grid =  [
    #             ["1","1","1","1","0"],
    #             ["1","1","0","1","0"],
    #             ["1","1","0","0","0"],
    #             ["0","0","0","0","0"],
    #         ]

    grid =  [
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"],
            ]

    sol = Solution()
    ans = sol.numIslands(grid)
    print(ans)
