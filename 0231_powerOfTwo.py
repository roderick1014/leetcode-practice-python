# 0231 - Power of Two

'''
    Question:
        Given an integer n, return true if it is a power of two. Otherwise, return false.

        An integer n is a power of two, if there exists an integer x such that n == 2^x.
'''



class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n > 0) and not (n & (n - 1))

if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfTwo(256))