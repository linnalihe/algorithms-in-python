# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573730-921950-1127-6897
# all tests passed

def segregate_evens_and_odds(numbers):
    # lomuto's partition for 2 partitions
    left = -1
    for idx in range(len(numbers)):
        if numbers[idx] % 2 == 0:
            left+=1
            numbers[idx], numbers[left] = numbers[left], numbers[idx]
            
    return numbers