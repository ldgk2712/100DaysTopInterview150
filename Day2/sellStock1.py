class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            if minPrice > price:
                minPrice = price
            else:
                profit = price - minPrice
                maxProfit = max(maxProfit, profit)
        return maxProfit

s = Solution()
print(s.maxProfit([7,1,5,3,6,4])) # 5