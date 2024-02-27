from collections import defaultdict

def minWindow(s: str, t: str) -> str:

    if len(s) < len(t) or t == "":
        return ""
    # bruteforce is to create all substring and check that all chars
    # in t are included and update minimum => O(n^2)
    # track needed chars and total needed chars
    # track have chars and total have chars
    # update the have map and have count and if count equal, attemp to update output
    # increment left pointer until have count is less than needed
    output = [-1, -1]
    outlen = float("inf")

    need_val_map = defaultdict(int)
    for char in t:
        need_val_map[char] +=1

    need_count = len(need_val_map)
    

    have_count = 0
    have_val_map = defaultdict(int)

    left = 0
    right = 0

    while right < len(s):
        have_val_map[s[right]] +=1
        if s[right] in need_val_map and have_val_map[s[right]] == need_val_map[s[right]]:
            have_count +=1

        while have_count == need_count:

            substr_len = right-left+1
            if substr_len < outlen:
                output = [left, right]
                outlen = right-left+1

            have_val_map[s[left]] -=1
            if s[left] in need_val_map and have_val_map[s[left]] < need_val_map[s[left]]:
                have_count-=1

            left+=1

        right+=1

    left, right = output
    return s[left:right+1] if outlen != float('inf') else ""