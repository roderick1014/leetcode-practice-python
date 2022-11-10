# 0070 - Climbing Stairs

'''
    Question:
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps.
        In how many distinct ways can you climb to the top?
'''

class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.climb(n) 

    def climb(self, n):
        if n <= 2: return n
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for idx in range(3, n + 1):
            dp[idx] = dp[idx - 1] + dp[idx - 2]

        return dp[n]

if __name__ == '__main__':
    n = 30
    sol = Solution()
    print(sol.climbStairs(n))


