# https://uplevel.interviewkickstart.com/resource/rc-codingproblem-573747-949567-250-1586
# passed tests
# space: pair_map,  visited, dfs stack => O(N) * 3 worse case
# time: create pair_map, dfs, iterate pair map => O(N) * 3 worse case

from collections import defaultdict
def number_of_connected_components(n, edges):
    """
    Args:
     n(int32)
     edges(list_list_int32)
    Returns:
     int32
    """
    # param n: number of pairs in edges list
    # param edges: list of pairs of integers that are connected
    # create a map of from edges
    # iterate through the map to count components
    count = 0
    pair_map = defaultdict(list)
    for pair1, pair2 in edges:
        pair_map[pair1].append(pair2)
        pair_map[pair2].append(pair1)
        
    visited = set()
    
    def dfs(key):
        visited.add(key)
        for val in pair_map[key]:
            if val not in visited:
                dfs(val)
    
    key_count = 0
    for key, val in pair_map.items():
        key_count+=1
        if key not in visited:
            count+=1
            dfs(key)
            
    singles = n - key_count
        
    
    return count + singles