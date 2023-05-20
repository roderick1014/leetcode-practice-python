# 0168 - Excel Sheet Column Title

'''
    Question:
        Given an integer columnNumber, 
        return its corresponding column 
        title as it appears in an Excel sheet.
'''

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """

        # ord('A') returns the ASCII value of 'A'. 
        # chr() will return the capital corresponding to the ASCII value.
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        ans = []
        while columnNumber > 0:
            # columnNumber - 1 to get a number range from 0 to 25 (Since index 0 -> 'A')
            ans.append(capitals[((columnNumber - 1) % 26)])     
            columnNumber = (columnNumber - 1) // 26
        ans.reverse()

        return ''.join(ans)



if __name__ == '__main__':
    columnNumber = 701
    sol = Solution()
    print(sol.convertToTitle(columnNumber))