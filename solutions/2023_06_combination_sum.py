# https://leetcode.com/problems/combination-sum/description/

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        candidates is list of int, target is an int
        ouput is list of list of int
        generate all the combinations
            example 1 combos: [2, 2, 2, 2], [2, 2, 2, 3]
            for each int, you can choose from the list again inclusive of same int
            each time you pick, include number and exclude number
            depth first search as long as sum is less than target, find all combos
            have a set to keep track of seen
        check if ints in combo sum to target
        add to output if sum == target, else skip

        """

        output = []

        def backtrack(curr_combo, idx):
            curr_sum = sum(curr_combo)
            if curr_sum == target:
                output.append(curr_combo)
                return

            elif curr_sum > target:
                return

            elif curr_sum < target:

                for j in range(idx, len(candidates)):
                    backtrack(curr_combo + [candidates[j]], j)

        backtrack([], 0)

        return output