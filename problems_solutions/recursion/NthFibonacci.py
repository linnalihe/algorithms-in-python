def getNthFib(n, memo={1: 0, 2: 1}):
    if n in memo:
        return memo[n]
    memo[n] = getNthFib(n-1, memo) + getNthFib(n-2, memo)

    return memo[n]


def getNthFib2(n):
    memo = [None]*(n+1)
    return getFib(n, memo)


def getFib(n, memo):
    if memo[n] is not None:
        return memo[n]
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        memo[n] = getFib(n-2, memo) + getFib(n-1, memo)

    return memo[n]


def getNthFib3(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    lastTwo = [0, 1]
    count = 2
    while count < n:
        third = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = third
        count += 1
    return lastTwo[1]
