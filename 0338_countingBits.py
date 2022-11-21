# 0338 - Counting Bits

'''
    Question:
        Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
'''

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        counter = [0]

            # We can divide the problem to be left-part (previous calculation) and right-part (check the new bit).

        for i in range(1, n + 1):

            counter.append(counter[i >> 1] + i % 2)     
            # With counter[i >> 1] we can leverage previous results. 
            # Ex: If we want to check 1111 or 1110, we can check counter[i >> 1] which is the result of 111 
            # (Note that i is the number that we currently calculated.).
            # Eventually, we will check the if the right-most bit is '1' by using i % 2.
            # 

        return counter
        

if __name__ == '__main__':
    
    n = 5
    sol = Solution()
    print(sol.countBits(n))