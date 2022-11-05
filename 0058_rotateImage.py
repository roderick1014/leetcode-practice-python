# 0058 - Rotate Image

'''
    Question:
        You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
        You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
'''


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        # Method: Do (1) row-wise reverse and (2) flip the matrix with respective to the "↘" diagonal line.

        # Example: [1, 2, 3]        [7, 8, 9]       [7, 4, 1]
        #          [4, 5, 6]    →   [4, 5, 6]   →   [8, 5, 2]  OK!
        #          [7, 8, 9]        [1, 2, 3]       [9, 6, 3]
        
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

if __name__ == '__main__':
    matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
             ]

    sol = Solution()
    sol.rotate(matrix)
    print(matrix)