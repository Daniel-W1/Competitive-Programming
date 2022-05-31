class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_cnt = 0
        for key in count:
            cnt = 1
            check = not count.get(key-1,False)
            while count.get(key+1,False) and check:
                cnt += 1
                key += 1
            max_cnt = max(max_cnt,cnt)
        return max_cnt
    
                
                
                
        