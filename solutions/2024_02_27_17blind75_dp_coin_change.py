# https://leetcode.com/problems/coin-change/
# all tests passed
def coinChange(coins: list[int], amount: int) -> int:
        
        coin_map = [float("inf")] * (amount+1)
        coin_map[0] = 0

        for idx in range(amount+1):
            for coin in coins:
                diff = idx - coin
                if diff >= 0:
                    coin_map[idx] = min(coin_map[idx], coin_map[diff] +1)

        return coin_map[amount] if coin_map[amount] != float("inf") else -1