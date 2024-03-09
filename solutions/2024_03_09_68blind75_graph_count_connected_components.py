# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573747-949567-250-1586
# all tests passed
def number_of_connected_components(n, edges):
    # create adjacency list
    # count components
    
    count = 0
    
    adjlist = [[] for _ in range(n)]
    for n1, n2 in edges:
        adjlist[n1].append(n2)
        adjlist[n2].append(n1)
        
    visited = set()
    
    def dfs(node):
        
        if node in visited:
            return
        
        visited.add(node)
        for neigh in adjlist[node]:
            dfs(neigh)
        
    for node in range(n):
        if not node in visited:
            count+=1
            dfs(node)

    
    return count