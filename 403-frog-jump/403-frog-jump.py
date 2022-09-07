class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = [set() for _ in range(len(stones))]
        # base case 
        dp[0] = [0]
        
        for idx, jumps in enumerate(dp):
            cur_pos = stones[idx]
            for jump in jumps:
                choices = [jump + change for change in range(-1, 2)]
                for choice in choices:
                    if choice > 0:
                        new_pos = bisect.bisect_left(stones, cur_pos + choice)
                        if new_pos < len(dp) and stones[new_pos] == cur_pos + choice:
                            dp[new_pos].add(choice)
        return bool(dp[-1])