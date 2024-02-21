# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573730-921950-1127-6898
# passed all tests
def merge_one_into_another(first, second):
    # bruteforce is to copy array in second into another container
    # iterate through first and copy of 2nd to put back into second
    # uses extra space and takes time to copy
    # better to use the end of the array and pull out largest value
    # to fill in second array in descending order
    # pointer at end of first, and at same position in second
    # time is O(2n) to go thorugh all elements, space is O(1) bc using second array
    
    oneidx = len(first)-1
    twoidx = len(first)-1
    fill_idx = len(second)-1
    while oneidx >= 0 and twoidx >= 0:
        if first[oneidx] >= second[twoidx]:
            second[fill_idx] = first[oneidx]
            oneidx-=1
        else:
            second[fill_idx] = second[twoidx]
            twoidx-=1
            
        fill_idx-=1
    
    while oneidx >= 0:
        second[fill_idx] = first[oneidx]
        oneidx-=1
        fill_idx-=1
        

    return second