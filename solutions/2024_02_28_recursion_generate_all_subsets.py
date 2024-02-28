# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573733-927405-1032-6301
# all tests passed 
def generate_all_subsets(s):
    # using a temp variable that is a new string with appended value
    # O(2^n)
    
    res = []
    
    def make_subsets(idx, temp):
        if idx == len(s):
            res.append(temp)
            return
            
        make_subsets(idx+1, temp+s[idx])
        make_subsets(idx+1, temp)
    
    make_subsets(0, "")
    return res