

NEIGHBORS = {
    1: (6,8),
    2: (7,9),
    3: (4,8),
    4: (3,9,0),
    5: tuple(),
    6: (1,7,0),
    7: (2,6),
    8: (1,3),
    9: (2,4),
    0: (4,6)
}

def knights_dialer(n:int, pos:int):

    if n == 0:
        return 1
    
    dial_count = 0
    for val in NEIGHBORS(pos):
        dial_count += knights_dialer(n-1, val)

    return dial_count

    