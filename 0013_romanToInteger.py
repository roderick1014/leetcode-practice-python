# 0013 - Roman to Integer

'''
    Question:
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

                Symbol       Value
                I             1
                V             5
                X             10
                L             50
                C             100
                D             500
                M             1000

        For example, 2 is written as II in Roman numeral, just two ones added together. 
        12 is written as XII, which is simply X + II. 
        The number 27 is written as XXVII, which is XX + V + II.

        - I can be placed before V (5) and X (10) to make 4 and 9. 
        - X can be placed before L (50) and C (100) to make 40 and 90. 
        - C can be placed before D (500) and M (1000) to make 400 and 900.
'''



class Solution(object):

    def romanToInt(self, s):

        """
        :type s: str
        :rtype: int
        """
        
        roman2Integer = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        # If the value of a Roman in the next element is larger than the previous one, the current number should be subtracted. 
        # For example: VI = 5 + 1 = 6, IV = -1 + 5 = 4
        
        ans = 0

        for idx in range(len(s) - 1):

            # Subtract the current value.
            if roman2Integer[s[idx]] < roman2Integer[s[idx + 1]]:
                ans = ans - roman2Integer[s[idx]]
            else:
                ans = ans + roman2Integer[s[idx]]

        return ans + roman2Integer[s[-1]]


if __name__ == '__main__':

    s = 'III'       # 3
    s = 'LVIII'     # 58
    s = 'MCMXCIV'   # 1994

    sol = Solution()
    print(sol.romanToInt(s))  