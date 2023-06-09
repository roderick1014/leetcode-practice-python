# 0036 - Valid Sudoku

'''
    Question:
        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        - Each row must contain the digits 1-9 without repetition.
        - Each column must contain the digits 1-9 without repetition.
        - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        Note:
            A Sudoku board (partially filled) could be valid but is not necessarily solvable.
            Only the filled cells need to be validated according to the mentioned rules.
'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.colValid(board) and self.rowValid(board) and self.matrixValid(board)

    def rowValid(self, board):
        for row in board:
            if not self.isValid(row):
                return False
        return True

    def colValid(self, board):
        # zip() function is used to combine multiple iterables (such as lists, tuples, or strings)
        # as input and returns an iterator that produces tuples of corresponding elements from these iterables.
        # It "zips" or pairs up the elements based on their index.
        for col in zip(*board):
            if not self.isValid(col):
                return False
        return True

    def matrixValid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                # i, j >> 0 ~ 3 / 3 ~ 6 / 6 ~ 9
                sample = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.isValid(sample):
                    return False
        return True

    def isValid(self, sample):
        sample = [element for element in sample if element != '.']
        return len(sample) == len(set(sample))

if __name__ == '__main__':
    board = \
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

    sol = Solution()
    print(sol.isValidSudoku(board))