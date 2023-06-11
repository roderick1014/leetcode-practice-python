# 0289 - Game of Life

'''
    Question:
        According to Wikipedia's article:
            "The Game of Life, also known simply as Life,
                is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

        The board is made up of an m x n grid of cells, where each cell has an initial state:

        -> live (represented by a 1) or dead (represented by a 0).

        Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using
        the following four rules (taken from the above Wikipedia article):

        - Any live cell with fewer than two live neighbors dies as if caused by under-population.
        - Any live cell with two or three live neighbors lives on to the next generation.
        - Any live cell with more than three live neighbors dies, as if by over-population.
        - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        - The next state is created by applying the above rules simultaneously to every cell in the current state,
            where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # Unchange case: live cell 1 -> 1, die cell 0 -> 0
        # Change case: live cell 1 -> 2, die cell 0 -> -1 (2 denotes dead cell, -1 denotes live cell)
        # Determine live before: board[row][col] > 0
        # Determine dead before: board[row][col] <= 0

        row_length = len(board)
        col_legth = len(board[0])
        directions = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]

        for row in range(row_length):
            for col in range(col_legth):

                neighbor_state = 0

                for row_shift, col_shift in directions:
                    d_row = row + row_shift
                    d_col = col + col_shift

                    if 0 <= d_row <= (row_length - 1) and 0 <= d_col <= (col_legth - 1) and board[d_row][d_col] > 0:
                        neighbor_state += 1

                # Apply condition
                if board[row][col] == 1 and (neighbor_state > 3 or neighbor_state < 2): # overpopulation / under-population (dead)
                    board[row][col] = 2  # 1 -> 2
                elif board[row][col] == 0 and neighbor_state == 3:
                    board[row][col] = -1  # 0 -> -1

        for row in range(row_length):
            for col in range(col_legth):
                if board[row][col] == 2:
                    board[row][col] = 0
                elif board[row][col] == -1:
                    board[row][col] = 1

        # # Solution 1 - Old
        # row_length = len(board)
        # col_legth = len(board[0])

        # for row in range(row_length):
        #     for col in range(col_legth):

        #         neighbor_state = 0
        #         if row != 0 and board[row - 1][col] > 0:       # top
        #             neighbor_state += 1

        #         if row != (row_length - 1) and board[row + 1][col] > 0: # bottom
        #             neighbor_state += 1

        #         if col != 0 and board[row][col - 1] > 0: # left
        #             neighbor_state += 1

        #         if col != (col_legth - 1) and board[row][col + 1] > 0: # right
        #             neighbor_state += 1

        #         if row != 0 and col != (col_legth - 1) and board[row - 1][col + 1] > 0: # right-top
        #             neighbor_state += 1

        #         if row != 0 and col != 0 and board[row - 1][col - 1] > 0: # left-top
        #             neighbor_state += 1

        #         if row != (row_length - 1) and col != (col_legth - 1) and board[row + 1][col + 1] > 0: # right-bottom
        #             neighbor_state += 1

        #         if row != (row_length - 1) and col != 0 and board[row + 1][col - 1] > 0: # left-bottom
        #             neighbor_state += 1

        #         # Apply condition
        #         if board[row][col] == 1 and (neighbor_state > 3 or neighbor_state < 2): # overpopulation / under-population (dead)
        #             board[row][col] += 1  # 1 -> 2
        #         elif board[row][col] == 0 and neighbor_state == 3:
        #             board[row][col] -= 1  # 0 -> -1

        # for row in range(row_length):
        #     for col in range(col_legth):
        #         if board[row][col] == 2:
        #             board[row][col] -= 2
        #         if board[row][col] == -1:
        #             board[row][col] += 2


if __name__ == '__main__':
    board = [
                [0,1,0],
                [0,0,1],
                [1,1,1],
                [0,0,0],
            ]
    sol = Solution()
    sol.gameOfLife(board)
    print(board)