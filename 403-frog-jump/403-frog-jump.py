class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = {}
        def cross(idx, prevjump):
            if (idx, prevjump) in memo: return memo[idx, prevjump]
            if idx == stones[-1]:
                return True
            if idx > stones[-1]:
                return False
            
            pos = bisect.bisect_left(stones, idx)
            # print(idx, "here", stones[pos])
            if stones[pos] != idx:
                return False
            # i can always assume i start from index 1
            if prevjump - 1 > 0:
                memo[idx, prevjump] = cross(idx + prevjump-1, prevjump-1) or cross(idx + prevjump, prevjump) or cross(idx + prevjump+1, prevjump+1)
                return memo[idx, prevjump]
            else:
                memo[idx, prevjump] = cross(idx + prevjump, prevjump) or cross(idx + prevjump+1, prevjump+1)
                return memo[idx, prevjump]
        return cross(1, 1)