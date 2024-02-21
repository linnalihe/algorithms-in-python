
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

def divideArray( nums: list[int], k: int) -> list[list[int]]:
        # param nums: list of ints positive, length n, multiple of 3
        # param k: positive integer
        # return list of ints bucketed
        nums.sort()
        output =[]
        temp = [nums[0]]
        for idx in range(1, len(nums)):
            number = nums[idx]
            if len(temp) == 3:
                output.append(temp.copy())
                temp = [number]
            else:
                if (number - temp[0] > k) :
                        return []
                temp.append(number)

        output.append(temp)
                
        return output
# Sample tests
# [1,3,4,8,7,9,3,5,1]
# 2
# [1,3,3,2,7,3]
# 3