# 0322 - Coin Change

'''
    Question:
        You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
        Return the fewest number of coins that you need to make up that amount. 
        If that amount of money cannot be made up by any combination of the coins, return -1.
        You may assume that you have an infinite number of each kind of coin.
'''

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        # Needs DP-Bottom Up method.
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        '''
            Ex -> coins = [1, 3, 4, 5], amount = 7.

            DP table:
                # ================================================================== #
                | amount | 1 | 2 | 3 | 4 | 5 | 6 | 7 | => (Array index)
                | -------|---|---|---|---|---|---|---|
                |  coins | 1 | 2 | 1 | 1 | 1 | 2 | ? | => (Elements, num of coins)
                # ================================================================== #
        '''

        for amnt in range(1, amount + 1):
            for coin in coins:
                if amnt - coin >= 0:
                    dp[amnt] = min(dp[amnt], 1 + dp[amnt - coin])
                    # =============================================================================================================
                    #   dp[amnt - coin] checks the previous path in DFS, knowing the result faster.
                    #   For example, if dp[1] = float('inf'), current_amount = 4, coin = 3, dp[current_amount] = 4.
                    #   Thus, dp[amnt] = min(dp[amnt], 1 + dp[amnt - coin]) 
                    #   -> "dp[amount - coin]" indicates the remaining coins to collect (the needed number of coins is stored here.)
                    #   -> which we can trace back to the previous answer and obtain the result immediately.
                    # =============================================================================================================

        return dp[-1] if dp[-1] != float('inf') else -1
        

if __name__ == '__main__':
    coins = [3, 7]
    amount = 7
    sol = Solution()
    print(sol.coinChange(coins, amount))