# 0054 - Spiral Matrix

'''
    Question:
        Given an m x n matrix, return all elements of the matrix in spiral order.
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # Solution 2 - Bound traversing (Simpler)
        res =[]

        l = 0
        r = len(matrix[0]) - 1
        t = 0
        b = len(matrix) - 1

        while len(res) < (len(matrix[0] * len(matrix))):
            i = l
            while i <= r:
                res.append(matrix[t][i])
                i += 1
            t += 1
            i = t
            if len(res) == (len(matrix[0] * len(matrix))):
                break
            while i <= b:
                res.append(matrix[i][r])
                i += 1
            r -= 1
            i = r
            if len(res) == (len(matrix[0] * len(matrix))):
                break
            while i >= l:
                res.append(matrix[b][i])
                i -= 1
            b -= 1
            i = b
            if len(res) == (len(matrix[0] * len(matrix))):
                break
            while i >= t:
                res.append(matrix[i][l])
                i -= 1
            l += 1

        return res

        # # Solution 1 - Intuitive
        # row_len = row_target = len(matrix)
        # col_len = col_target = len(matrix[0])
        # if col_len == 1 and row_len == 1: return [matrix[0][0]]
        # if row_len == 1: return matrix[0]
        # ans = []
        # col, row, col_shift, row_shift = 0, 0, 1, 1
        # switch, switch_cnt = 0, (col_len + row_len) - 1
        # total_cnt = 0
        # total = col_len * row_len

        # while total_cnt < total:
        #     cnt = 0
        #     for col in range(col, col_target, col_shift):
        #         ans.append(matrix[row][col])
        #         cnt += 1
        #         total_cnt += 1

        #     row += row_shift
        #     col_shift *= -1

        #     for row in range(row, row_target, row_shift):
        #         ans.append(matrix[row][col])
        #         cnt += 1
        #         total_cnt += 1

        #     col += col_shift
        #     row_shift *= -1

        #     if cnt == switch_cnt:
        #         switch_cnt -= 2
        #         switch += 1
        #         if switch % 2 == 0:
        #             col_len -= 1
        #             row_len -= 1
        #             col_target = col_len
        #             row_target = row_len
        #         else:
        #             col_target = -1 + (switch // 2)
        #             row_target = 0 + (switch // 2)
        # return ans

if __name__ == '__main__':
    matrix = [
                [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
            ]
    # matrix = [
    #             [1,2,3],
    #             [4,5,6],
    #             [7,8,9],
    #         ]
    # matrix = [[7],[9],[6]]

    sol = Solution()
    print(sol.spiralOrder(matrix))