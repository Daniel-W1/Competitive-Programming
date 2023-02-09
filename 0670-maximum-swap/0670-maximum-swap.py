class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        cur_max = -1

        next_max = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):

            next_max[i] = cur_max
            if nums[i] > nums[cur_max]:
                cur_max = i


        for i, val in enumerate(nums):
            if nums[i] < nums[next_max[i]]:
                nums[i] , nums[next_max[i]] = nums[next_max[i]] , nums[i]
                break

        newNum = "".join(nums)

        return int(newNum)