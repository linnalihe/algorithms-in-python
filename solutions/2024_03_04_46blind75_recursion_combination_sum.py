# https://leetcode.com/problems/combination-sum/
# all tests passed
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:

    output = []

    def get_combos(idx, currsum, temp):

        if currsum > target or idx >= len(candidates):
            return

        if currsum == target:
            output.append(temp.copy())
            return

        temp.append(candidates[idx])
        get_combos(idx, currsum+candidates[idx], temp)
        temp.pop()
        get_combos(idx+1, currsum, temp)
    

    get_combos(0, 0, [])
    return output