
# Non-Constructible Change
# Given positive, find the minimum change that can't be created.

def nonConstructibleChange(coins):
    coins.sort()
    coinSum = 0
    for c in coins:
        prevSum = coinSum
        coinSum += c
        if(prevSum + 1 < c):
            return prevSum + 1

    if(len(coins) > 0):
        return sum(coins)+1
    else:
        return 1
