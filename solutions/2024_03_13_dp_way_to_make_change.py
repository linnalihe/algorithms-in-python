
# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573753-958553-248-1566
# all tests passed
def number_of_ways(coins, amount):


    # top down is to recursively count by including coin at idx and excluding coin at index
    # base case is if target < 0 return 0; if idx < 0 and target is 0 return 1
    # bottom up dp is by using a matrix where first column rep number of ways to make 0 which is 1
    # each row rep the coins and count number of ways to make each val up to amount with that coin
    # condense into 1 array by overwritting each val idx with itself plus val at (idx - current coin)
    countmap = [0 for _ in range(amount+1)]
    countmap[0] = 1
    
    for c in coins:
        for a in range(c, amount+1):
            countmap[a] = (countmap[a] + countmap[a-c]) % 1000000007
    
    return countmap[amount]