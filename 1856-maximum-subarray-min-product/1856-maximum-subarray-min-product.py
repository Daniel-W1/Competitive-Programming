class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        stack = []
        nums = [0] + nums + [0]
        prefixSum = list(accumulate(nums))
        answer = 0
        mod = 10**9 + 7
        
        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                curidx = stack.pop()
                rangeSum = prefixSum[idx-1] - prefixSum[stack[-1]]
                answer = max(answer,(nums[curidx] *(rangeSum)))
            stack.append(idx)

        return answer % mod
                
                