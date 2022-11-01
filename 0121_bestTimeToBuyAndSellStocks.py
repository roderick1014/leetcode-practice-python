# 0121 - Best Time to Buy and Sell Stock

'''
    Question:
        Given an array prices where prices[i] is the price of a given stock on the ith day.
        To maximize the profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
'''

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        l_ptr = 0
        r_ptr = 1

        while r_ptr < len(prices):
            
            if (prices[r_ptr] > prices[l_ptr]):
                current_profit = prices[r_ptr] - prices[l_ptr]
                max_profit = max(current_profit, max_profit)
            else:
                l_ptr = r_ptr

            r_ptr += 1

        return max_profit


if __name__ == '__main__':

    prices = [1,4,2]

    sol = Solution()
    ans = sol.maxProfit(prices)
    print(ans)