from collections import defaultdict
def find_order(words):
    """
    Args:
     words(list_str)
    Returns:
     str
    """
    # param words: list of strings sorted
    # return string of chars in sorted order
    # will i get empty list? will chars be letters in alphabet? empty strings?
    # example 1:
    # b > a, b > c
    # d > a
    # b > d
    # create a directed graph, use dfs with topological sort
    # time: createing graph iterate words O(N*M) where N is words, M is lenght of words
    # topological sort with dfs O(N+E)
    # total: O(N*M)
    # space: need graph adjacency map O(N), dfs stack is O(N+E), output is letters max length 26 O(1)
    # total is O(N+E)
    arrival = {}
    departure = {}
    time = [0]
    output = []
    adj_map = defaultdict(list)
    for idx in range(len(words)-1):
        pt = 0
        while pt < len(words[idx]) and pt < len(words[idx+1]):
            if words[idx][pt] == words[idx+1][pt]:
                pt+=1
            else:
                adj_map[words[idx][pt]].append(words[idx+1][pt])
                break
            
    def dfs(key, time, output):
        
        
        arrival[key] = time
        time[0] +=1
        for dependent in adj_map.get(key, []):
            if arrival.get(dependent, -1) == -1:
                dfs(dependent, time, output)
            
        output.append(key)
        departure[key] = time
        time[0] +=1
            
    
    for key in adj_map.keys():
        # if not visited yet
        if arrival.get(key, -1) == -1:
            dfs(key, time, output)
        
    
    if len(output) == 0 and len(words) > 0:
        return words[0][0]
    
    output.reverse()
    return ''.join(output)