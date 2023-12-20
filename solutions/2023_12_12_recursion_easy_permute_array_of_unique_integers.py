# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573733-927405-1032-6298
# test passed
def get_permutations(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_list_int32
    """
    # param arr: list of numbers to create permutations from
    # return list of al the permutations created from arr
    # check that the length of the created permutation is equal to the length of arr
    # time: O(n^n!) where each n space has n! options
    # space: same as time
    
    res = []
    
    def make_permutations(arr, temp):
        if len(temp) == len(arr):
            res.append(temp.copy())
            return
        
        for each in arr:
            if each not in temp:
                temp.append(each)
                make_permutations(arr, temp)
                temp.pop()
            
    make_permutations(arr, [])
    
    return res
