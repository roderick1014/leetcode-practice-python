# 0073 - Set Matrix Zeroes

'''
    Question:
        Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
        You must do it in place.

        - A straightforward solution using O(mn) space is probably a bad idea.
        - A simple improvement uses O(m + n) space, but still not the best solution.
        - Could you devise a constant space solution O(1)?
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # Solution 2 - Reverse traversal
        firstRowVal, R, C = 1, len(matrix), len(matrix[0])

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0 # mark column
                    if i != 0:
                        matrix[i][0] = 0
                    else:
                        firstRowVal = 0

        for i in reversed(range(R)):
            for j in reversed(range(C)):
                if i == 0:
                    matrix[i][j] *= firstRowVal
                elif matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # # Solution 1 - Check border and set 0
        # fisrt_row_zero = False
        # fisrt_col_zero = False

        # for row in range(len(matrix)):
        #     for col in range(len(matrix[0])):
        #         if matrix[row][col] == 0:
        #             matrix[0][col] = 0
        #             matrix[row][0] = 0
        #             fisrt_row_zero = fisrt_row_zero or (row == 0)
        #             fisrt_col_zero = fisrt_col_zero or (col == 0)

        # for row in range(1, len(matrix)):
        #     for col in range(1, len(matrix[0])):
        #         if matrix[row][0] == 0 or matrix[0][col] == 0:
        #             matrix[row][col] = 0
        # if fisrt_row_zero:
        #     for col in range(len(matrix[0])):
        #         matrix[0][col] = 0

        # if fisrt_col_zero:
        #     for row in range(len(matrix)):
        #         matrix[row][0] = 0



if __name__ == '__main__':
    matrix = [
                [1,1,1],
                [1,0,1],
                [1,1,1],
            ]
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    sol = Solution()
    sol.setZeroes(matrix)
    print(matrix)