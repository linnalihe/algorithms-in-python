# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573734-932484-1142-7058
# all tests passed

def generate_all_subsets(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # param s: a string for creating all subsets from
    # return a list of subsets of s
    # can either include or exclude each char of s, each include or exclude will move the function forward
    # base case is when pointer is 0
    
    res = []
    
    def get_subsets(idx, temp):
        if idx == len(s):
            res.append(temp)
            return
            
        get_subsets(idx+1, temp+s[idx])
        get_subsets(idx+1, temp)
            
    get_subsets(0, "")
    
    return res