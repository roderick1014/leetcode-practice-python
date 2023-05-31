# 0342 - Power of Four

'''
    Quesion:
        Given an integer n, return true if it is a power of four. 
        Otherwise, return false.

        An integer n is a power of four, 
        if there exists an integer x such that n == ^4x.
'''

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n & (n-1) == 0 and (n - 1) % 3 == 0 
    
if __name__ == '__main__':
    n = 16
    sol = Solution()
    print(sol.isPowerOfFour(n))