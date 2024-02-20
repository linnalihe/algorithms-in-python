# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573730-921950-1127-6902
# all tests passed
def dutch_flag_sort(balls):

    # use lomuto's partitioning to divide up the colors into 3 partitions
    left = -1
    middle = -1
    for idx in range(len(balls)):
        
        if balls[idx] == "G":
            left +=1
            balls[idx], balls[left] = balls[left], balls[idx]
        if balls[idx] == "R":
            left+=1
            balls[idx], balls[left] = balls[left], balls[idx]
            middle+=1
            balls[middle], balls[left] = balls[left], balls[middle]
            
    return balls