# 0326 - Power of Three

'''
    Question:
        Given an integer n, return true if it is a power of three. Otherwise, return false.
        An integer n is a power of three, if there exists an integer x such that n == 3x.
'''

import math

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        return (round((math.log(n)/math.log(3)),10)) % 1.0 == 0

if __name__ == '__main__':
    n = 243
    sol = Solution()
    print(sol.isPowerOfThree(n))