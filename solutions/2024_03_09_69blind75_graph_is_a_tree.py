# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573747-949567-250-1587
# all tests passed
def is_it_a_tree(node_count, edge_start, edge_end):
    # a tree if single component with no cycles
    # count components
    # check for cycles
    if node_count <= 0:
        return True
    
    adjlist = [[] for _ in range(node_count)]
    for idx in range(len(edge_start)):
        if edge_start[idx] == edge_end[idx]:
            return False
        adjlist[edge_start[idx]].append(edge_end[idx])
        adjlist[edge_end[idx]].append(edge_start[idx])
        
    
    count = 0
    visited = [-1 for _ in range(node_count)]
    
    def dfs_cycle(n):
    
        
        for neigh in adjlist[n]:
                
            if visited[neigh] == -1:
                visited[neigh] = n
                if dfs_cycle(neigh):
                    return True
            else:
                if visited[n] != neigh:
                    return True
        
        return False
            

    for n in range(node_count):
        if visited[n] == -1:
            visited[n] = 0
            count +=1
            if count > 1:
                return False
            if dfs_cycle(n):
                return False
            
    return True