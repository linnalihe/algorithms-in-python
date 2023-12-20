# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573733-927405-1032-6361
# all tests passed
def get_binary_strings(n):
    """
    Args:
     n(int32)
    Returns:
     list_str
    """
    # param n: the length of the strings being generated
    # return a list of all the possible binary strings of length n
    # each spot can either be 0 or 1
    # base case is when n < 1
    # time: call stack for recursive call O(n)
    # space: call stack for recursive call O(n), permutations of len n O(2^n) => O(2^n)
    res = []
    
    def get_binary_str(n, temp):
        if n < 1:
            res.append("".join(temp))
            return
        
        temp.append("0")
        get_binary_str(n-1, temp)
        temp.pop()
        temp.append("1")
        get_binary_str(n-1, temp)
        temp.pop()
            
    get_binary_str(n, [])
            
    return res