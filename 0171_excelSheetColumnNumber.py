# 0171 - Excel Sheet Column Number

'''
    Question:
        Given a string columnTitle that represents the column title
        as appears in an Excel sheet, return its corresponding column number.
'''

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        # Ex: ZYX:
        #   1 iter. ->  0 + 26
        #   2 iter. ->  26*26 + 25
        #   3 iter. ->  (26*26 + 25)*26 + 24 = 26*26^2 + 25*26^1 + 24*26^0

        ans = 0
        for capital in columnTitle:
            ans = ans * 26 + ord(capital) - ord('A') + 1
        return ans


if __name__ == '__main__':
    sol = Solution()

    columnTitle = "ZYX"
    print(sol.titleToNumber(columnTitle))