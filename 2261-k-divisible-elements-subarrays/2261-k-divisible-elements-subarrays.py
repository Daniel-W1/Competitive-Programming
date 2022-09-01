class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        lookup = set()
        ans = 0
        
        for start in range(len(nums)):
            cnt = 0
            cur = []
            for end in range(start, len(nums)):
                if not nums[end]%p:
                    cnt += 1
                cur.append(nums[end])
                if cnt <= k: 
                    if tuple(cur) in lookup: continue
                    ans += 1
                    lookup.add(tuple(cur))
                else:
                    break
        return ans
            
        