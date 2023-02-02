class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        
        cnt = defaultdict(int)
        
        for val in nums:
            if val:
                cnt[val] += 1
        
        return len(cnt)
