# 0006 - Zigzag Conversion

'''
    Question:
        The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
        (you may want to display this pattern in a fixed font for better legibility)
        P   A   H   N
        A P L S I I G
        Y   I   R
'''

class Solution(object):
    def convert(self, s: str, numRows: int) -> str:

            if numRows == 1:
                return s

            rows = ['' for _ in range(numRows)]

            row_idx = 0     # index to track which rows a character should be added to
            direction = 1   # 1 goes down, -1 goes up.
            for idx in range(len(s)):

                rows[row_idx] += s[idx]     # add the current character to corresponding row

                if row_idx == numRows - 1:        # if it reaches to the last row, we need to go up
                    direction = -1

                elif row_idx == 0:          # if it reaches to the first row, we need to go down
                    direction = 1

                row_idx += direction

            # rows would look like below in the first example
            # ['PAHN', 'APLSIIG', 'YIR']
            # we use join to build the final answer
            return ''.join(rows)

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3

    sol = Solution()
    print(sol.convert(s, numRows))