# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# all tests passed
def maxProfit(prices: list[int]) -> int:
        # bruteforce is to check each with every other O(n^2)
        # buy has to be a lesser idx than sell
        profit = 0
        buyidx = 0
        sellidx = buyidx+1
        while sellidx < len(prices):
            if prices[sellidx] > prices[buyidx]:
                profit = max(profit, prices[sellidx]-prices[buyidx])
            else:
                buyidx = sellidx
            
            sellidx+=1

        return profit