# Given two input arrays, one containing height of students with red shirts and one with height of students with blue shirts
# Return whether it's possible to take a photo where students in back row is taller than students in first row
# all red shirts must be in same row, all blue shirts must be in same row

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if(redShirtHeights[0] > blueShirtHeights[0]):
        for i in range(len(redShirtHeights)):
            if(redShirtHeights[i] <= blueShirtHeights[i]):
                return False
    else:
        for i in range(len(redShirtHeights)):
            if(redShirtHeights[i] >= blueShirtHeights[i]):
                return False

    return True
