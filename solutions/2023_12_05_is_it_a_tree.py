
# https://uplevel.interviewkickstart.com/resource/rc-codingproblem-573747-949567-250-1587
# time: 
# make adj list O(N) where N is len(edge_start) edge, 
# loop node_count O(M) where M is node_count, 
# dfs O(node+edge)
# total is O(node_count + edge)
# space: 
# visited parents O(node_count)
# adj_list O(node_count)
# dfs O(node_count + edge)
# total is O(node_count + edge)
# use dfs to count back edge for cycles and to mark visited to count components
# or use bfs to count cross edge for cycles and marke visited to count components
# make sure to check self loops, and visited nodes without parents as 0
def is_it_a_tree(node_count, edge_start, edge_end):
    """
    Args:
     node_count(int32)
     edge_start(list_int32)
     edge_end(list_int32)
    Returns:
     bool
    """
    # param node_count: number of nodes given
    # param edge_start: list of v1
    # param edge_end: list of v2
    # how big is input size? range of values?
    # type? negative? empty?
    # data structures used?
    # return true or false whether input is a tree
    # a tree is a single component without cycles
    # check that it's a single component - create adjacency list and count components
    # check cycles by seeing if we see a node we've already visited
    #   check for cross edge for bfs -> cross edge means theres cycle for bfs
    #   check of back edge for dfs -> back edge means theres cycle for dfs
    
    count = 0
    visited_parent = [-1 for _ in range(node_count)]
    adjlist = [[] for _ in range(node_count)]
    for i in range(len(edge_start)):
        if edge_start[i] == edge_end[i]:
            return False
        adjlist[edge_start[i]].append(edge_end[i])
        adjlist[edge_end[i]].append(edge_start[i])
        
    def dfs_is_cycle(node):
        
        for each in adjlist[node]:
            
            if visited_parent[each] == -1:
                visited_parent[each] = node
                if dfs_is_cycle(each):
                    return True
            else:
                if each != visited_parent[node]:
                    return True
        return False
                
        
    for i in range(node_count):
        
        if visited_parent[i] == -1:
            visited_parent[i] = 0
            count+=1
            if count > 1:
                return False
            if dfs_is_cycle(i):
                return False
            
        
    return True