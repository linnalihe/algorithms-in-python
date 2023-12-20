# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573733-927405-1032-6341
# all tests passed
def tower_of_hanoi(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_int32
    """
    # param n: n number of disks that need to be moved
    # delegate n-1 rest of disks to aux
    # current frame in change of moving the disk to the destination
    # delegate n-1 rest of disks to destination
    res = []
    def move_tower(n, src, aux, dest):
        if n == 1:
            res.append([src, dest])
            return
        
        
        move_tower(n-1, src, dest, aux)
        res.append([src, dest])
        move_tower(n-1, aux, src, dest)
        
    move_tower(n, 1, 2, 3)
        
    return res