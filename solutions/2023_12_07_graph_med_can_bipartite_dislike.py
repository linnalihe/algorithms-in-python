# https://uplevel.interviewkickstart.com/resource/rc-codingproblem-573747-949567-250-1588
# time: loop thru num_of_people O(N), dfs O(N+E) => O(N+E)
# space: adj_list O(N + E), dfs O(N+E) => O(N+E)
# dfs for coloring alternating nodes, use 0 and 1 but can also use a different coloring system
def can_be_divided(num_of_people, dislike1, dislike2):
    """
    Args:
     num_of_people(int32)
     dislike1(list_int32)
     dislike2(list_int32)
    Returns:
     bool
    """
    # :param num_of_people: number of people in town
    # :param dislike1: same len as dislike2, corresponding index is person dislike
    # :param dislike2: correspond to dislike1
    # return True if they can be split into different sets, else Fase
    # num_of_people integer? dislike1 and dislike2 directed or undirected? consider len 1 or empty?
    # create an adjacency list to represent graph
    # use dfs to alternate coloring of the nodes
    # if color can be alternating than True, else False
    
    
    persons_color = [-1 for _ in range(num_of_people)]
    
    adj_list = [[] for _ in range(num_of_people)]
    for idx in range(len(dislike1)):
        adj_list[dislike1[idx]].append(dislike2[idx])
        adj_list[dislike2[idx]].append(dislike1[idx])
        
    def dfs_color_person_alternate(person, color):
        if persons_color[person] != -1:
            return True
            
        persons_color[person] = color
        for p in adj_list[person]:
            # if they are the same color then there is a cycle
            if persons_color[p] == color:
                return False
            
            if not dfs_color_person_alternate(p, 1-color):
                return False
                
        return True
        
    
    for person in range(len(adj_list)):
        if persons_color[person] == -1:
            if not dfs_color_person_alternate(person, 0):
                return False
    
    return True
