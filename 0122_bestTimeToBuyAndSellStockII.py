# Best Time to Buy and Sell Stock II

'''
    Question:
        You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

        On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

        Find and return the maximum profit you can achieve.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
      
        # Time Complexity: O(n), for single level for loop.
        # Space Complexity: O(1), for fixed size of temporary variables.

        ans = 0
        cur = prices[0]
        
        for idx in range(len(prices)):
            if cur < prices[idx]:
                ans += (prices[idx] - cur)
            cur = prices[idx]

        return ans

if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    sol = Solution()
    print(sol.maxProfit(prices))