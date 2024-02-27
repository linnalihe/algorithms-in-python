# https://www.pramp.com/challenge/5j2xWAx1qPtlZGLnG2O0
# all tests passed
# top-down dp solution
def diffBetweenTwoStrings(source, target):
    ans = []
    i = 0
    j = 0

    seq_token = [[-1]*len(target) for _ in range(len(source))]

    def find_seq(sidx, tidx):
        if sidx == len(source):
            return len(target) - tidx
        elif tidx == len(target):
            return len(source) - sidx
        
        elif seq_token[sidx][tidx] == -1:
            if source[sidx] == target[tidx]:
                seq_token[sidx][tidx] = find_seq(sidx+1, tidx+1)
            else:
                seq_token[sidx][tidx] = 1+min(find_seq(sidx+1, tidx), find_seq(sidx, tidx+1))
        
        return seq_token[sidx][tidx]
        
    while i < len(source) and j < len(target):
        if source[i] == target[j]:
            ans.append(source[i])
            i+=1
            j+=1
            
        else:
            if find_seq(i+1, j) <= find_seq(i, j+1):
                ans.append('-' + source[i])
                i+=1
            else:
                ans.append('+' + target[j])
                j+=1
        
    while j < len(target):
        ans.append('+' + target[j])
        j+=1
    
  
    return ans

