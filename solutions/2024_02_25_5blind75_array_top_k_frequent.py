# https://leetcode.com/problems/top-k-frequent-elements/submissions/1186296337/
# all tests passed
from collections import defaultdict

def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    
    res =[]
    count_freq = defaultdict(int)
    for n in nums:
        count_freq[n] +=1

    count_bucket = [[] for _ in range(len(nums)+1)]
    for key, val in count_freq.items():
        count_bucket[val].append(key)

    for idx in reversed(range(len(count_bucket))):
        if len(count_bucket[idx]) > 0:
            for val in count_bucket[idx]:
                res.append(val)
                if len(res) == k:
                    return res