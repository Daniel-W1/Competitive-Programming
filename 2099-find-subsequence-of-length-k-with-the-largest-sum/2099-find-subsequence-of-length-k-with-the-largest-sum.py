class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = [(-val,i) for i,val in enumerate(nums)]
        ans = []
        while k:
            heapq.heapify(nums)
            ans.append(nums.pop(0))
            k -= 1
        ans = sorted(ans, key = lambda val:val[1])
        real_ans = [-val[0] for val in ans]
        return real_ans
        
        
                