# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573731-921952-245-1541
# all tests passed
def can_attend_all_meetings(intervals):
    """
    Args:
     intervals(list_list_int32)
    Returns:
     int32
    """
    # brute force is to compare each interval with all intervals
    # better to just check each interval with directly next to it
    # sort the intervals
    # compare 2nd value of each with 1st value of subsequent
    
    intervals.sort(key=lambda x:x[0])
    for idx in range(len(intervals)-1):
        if intervals[idx][1] > intervals[idx+1][0]:
            return 0
    
    return 1