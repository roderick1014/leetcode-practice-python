# 0191 - Number of One Bits

'''
    Question:
        Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
'''

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        cnt = 0

        while n:
            if (n & 1):
                cnt += 1
            n >>= 1         # Shift operation, which makes 0111 -> 0011 (remove the right-most bit).

        return cnt


if __name__ == '__main__':
    n = 3                   # Binary: 11
    sol =  Solution()
    print(sol.hammingWeight(n))