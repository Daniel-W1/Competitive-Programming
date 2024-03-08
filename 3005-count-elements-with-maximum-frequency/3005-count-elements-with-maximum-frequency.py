class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_seen = max_seen_cnt = 0
        cnt = defaultdict(int)
        
        for num in nums:
            cnt[num] += 1
            
            if cnt[num] > max_seen:
                max_seen = cnt[num]
                max_seen_cnt = 1
            elif cnt[num] == max_seen:
                max_seen_cnt += 1
        
        return max_seen * max_seen_cnt