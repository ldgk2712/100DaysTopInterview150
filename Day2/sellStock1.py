class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1,len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                profit = prices[i] - minPrice
                maxProfit = max(maxProfit, profit)
        return maxProfit

s = Solution()
print(s.maxProfit([7,6,4,3,1])) # 5