# Minimum Waiting Time

# sort the query in order
# add each query + the previous sum in a list, excluding the last item
# return the sum of the list which is the cumulative sum
def minimumWaitingTime(queries):
    queries.sort()
    sumlist = []
    c_sum = 0
    for i in range(len(queries)-1):
        c_sum = c_sum+queries[i]
        sumlist.append(c_sum)

    return sum(sumlist)


# O(n log(n)) time, O(1) space
def minimumWaitingTime2(queries):
    queries.sort()
    total = 0
    waitTime = 0
    for i in range(len(queries)-1):
        total = total + queries[i]
        waitTime += total

    return waitTime
