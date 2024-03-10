# https://uplevel.interviewkickstart.com/submissions/
# all tests passed
from collections import defaultdict
def find_order(words):
    # create adjmap for the words
    # if chars are differnt, add dependency
    # run post order dfs
    # return reversed output
    
    
    adjmap = defaultdict(list)
    for idx in range(len(words)-1):
        word1 = words[idx]
        word2 = words[idx+1]
        
        pt = 0
        while pt < len(word1) and pt< len(word2):
            
            if word1[pt] != word2[pt]:
                adjmap[word1[pt]].append(word2[pt])
                break
            pt+=1

    
    output = []
    visited = set()
    
    def dfs_post(curr):
        
        visited.add(curr)
        
        for dep in adjmap.get(curr, []):
            if not dep in visited:
                dfs_post(dep)
            
        output.append(curr)
        
    for key in adjmap:
        if not key in visited:
            dfs_post(key)
    
    if len(output) == 0 and len(words) > 0:
        output.append(words[0][0])
            
    output.reverse()
    return "".join(output)