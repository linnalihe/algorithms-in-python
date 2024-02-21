# all tests passed
def two_sum(numbers, target):
    # brute force is to compare each number with all numebrs O(n^2) time
    # can't sort because we need ot preserve index
    # better solution is to use a dictionary, only one pass so O(n) time, O(n) space to store all values
    # derive difference and compare it with seen numbers
    
    num_map = {}
    for idx, val in enumerate(numbers):
        diff = target - val
        if num_map.get(diff, -1) > -1:
            return [num_map.get(diff), idx]
        
        num_map[val] = idx
    
    
    return [-1, -1]