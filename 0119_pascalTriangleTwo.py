# 0119 - Pascal Triangle II

'''
    Question:
        Given an integer rowIndex, return the rowIndex-th (0-indexed) row of the Pascal's triangle.
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        record = []
        for i in range(rowIndex + 1):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = record[i - 1][j - 1] + record[i - 1][j]
            record.append(row)
        
        return record[-1]

if __name__ == '__main__':
    rowIndex = 1
    sol = Solution()
    print(sol.getRow(rowIndex))
