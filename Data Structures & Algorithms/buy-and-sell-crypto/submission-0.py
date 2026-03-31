class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        given int arr prices where each elem is price of neetcoin on ith day
        can choose any single day to buy one neetcoin and choose different day in future to sell
        return max profit we can achieve, can choose to not make any transactions, where profit would be 0

        prices = [10, 1, 5, 6, 7, 1]

        keep max_profit
        start two pointers and first elem

        buy, sell

        so start these at 
        buy would be 10
        sell would be 10

        max profit would be 0

        sell would move to 1, so no, then 
        """

        max_profit = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            else:
                buy = sell
            sell += 1

        return max_profit


