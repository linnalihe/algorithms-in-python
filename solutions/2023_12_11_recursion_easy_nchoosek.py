# https://uplevel.interviewkickstart.com/resource/rc-codingproblem-573733-927405-1032-6294
def find_combinations(n, k):
    """
    Args:
     n(int32)
     k(int32)
    Returns:
     list_list_int32
    """
    # param n: full set of numbers
    # param k: choose k numbers out of n
    # returns an array of all the combos for n choose k
    # call a recursive function where the base case checks if n == k or n is ==0 or == 1
    # append the temporary combos each time and take it out after
    
    all_combos = []
    
    def get_combos(n, k, temp_combos):
        
        if n <0:
            return
    
        if k == 0:
            all_combos.append(temp_combos.copy())
            return
            
        temp_combos.append(n)
        get_combos(n-1, k-1, temp_combos)
        temp_combos.pop()
        get_combos(n-1, k, temp_combos)
            
    get_combos(n, k, [])
        
    
    return all_combos