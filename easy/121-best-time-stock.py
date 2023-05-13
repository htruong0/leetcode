class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buyPrice = prices[0]
        for p in prices[1:]:
            if p > buyPrice:
                profit = max(profit, p - buyPrice)
            else:
                buyPrice = p
        return profit
    
if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    sol = Solution()
    a = sol.maxProfit(prices)
    print(a)
