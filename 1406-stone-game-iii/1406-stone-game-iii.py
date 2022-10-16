class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def dfs(idx, turn):
            if idx >= len(stoneValue):
                return 0
            
            if turn:
                choice1 = dfs(idx+1, 1 - turn) + stoneValue[idx]
                choice2, choice3 = -float('inf') ,-float('inf')
                if idx + 1 < len(stoneValue):
                    choice2 = dfs(idx + 2, 1 - turn) + stoneValue[idx] + stoneValue[idx+1]
                if idx + 2 < len(stoneValue):
                    choice3 = dfs(idx + 3, 1 - turn) + stoneValue[idx] + stoneValue[idx+1] + stoneValue[idx+2]
                
                return max(choice1, choice2, choice3)
            
            else:
                choice1 = dfs(idx+1, 1 - turn)
                choice2, choice3 = float('inf'), float('inf')
                if idx + 1 < len(stoneValue):
                    choice2 = dfs(idx + 2, 1 - turn)
                if idx + 2 < len(stoneValue):
                    choice3 = dfs(idx + 3, 1 - turn)
                return min(choice1, choice2, choice3)
        
        res = dfs(0, 1)
        # print(res)
        if res == sum(stoneValue)-res:
            return "Tie"
        elif res > sum(stoneValue)-res:
            return "Alice"
        return "Bob"
                
                
                