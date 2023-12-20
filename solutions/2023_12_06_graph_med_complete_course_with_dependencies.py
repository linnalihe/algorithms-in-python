
# https://uplevel.interviewkickstart.com/resource/rc-codingproblem-573747-949567-250-1591
# time
# space
#
def can_be_completed(n, a, b):
    """
    Args:
     n(int32)
     a(list_int32)
     b(list_int32)
    Returns:
     bool
    """
    # :param n: number of courses offered
    # :param a: the list of a must of taken before corresponding course at the same index in b
    # :param b: the list of courses that can be taken after a
    # create an adjacency list and traverse to check if there is a cycle
    # this is a directed graph
    # can be completed if there is a cycle, use dfs to check if there is a cycle
    # use arrival and departure time stamps to keep track of back edges
    # if the node is visited but has a departure time and your're seeing it again
    # that means there is a back edge and there is a cycle
    
    arrival = [-1 for _ in range(n)]
    departure = [-1 for _ in range(n)]
    time_stamp = 0
    visited = [-1 for _ in range(n)]
    adj_list = [[] for _ in range(n)]
    for idx in range(len(a)):
        adj_list[a[idx]].append(b[idx])
        
        
    def dfs_cycle_found(idx, time_stamp):
        arrival[idx] = time_stamp
        time_stamp+=1
        
        for each in adj_list[idx]:
            if visited[each] == -1:
                visited[each] = idx
                
                
                if dfs_cycle_found(each, time_stamp):
                    return True
            
            else:
                if departure[each] == -1:
                    return True
                    
        departure[idx] = time_stamp
        time_stamp+=1

                
        return False
                    
        
        
    
    for idx in range(n):
        if visited[idx] == -1:
            if dfs_cycle_found(idx, time_stamp):
                return False
        
        
    return True