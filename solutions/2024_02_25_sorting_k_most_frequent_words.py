# https://uplevel.interviewkickstart.com/resource/submissions/rc-codingproblem-573730-921950-1127-6941
# all tests passed
from collections import defaultdict
def k_most_frequent(k, words):
    """
    Args:
     k(int32)
     words(list_str)
    Returns:
     list_str
    """
    # brute force is to create a frequncy, make that into a list
    # for each item on the list,add to the result
    # time: make dict + sort + form result => O(n) + O(n log n) + O(k) => O(n log n)
    # space: dict + sorted list + result => O(n)
    word_freq = defaultdict(int)
    for w in words:
        word_freq[w] +=1
        
    sorted_words = sorted(word_freq.items(), key=lambda item: (-item[1], item[0]))
    result = [word[0] for word in sorted_words[:k]]
        

    return result