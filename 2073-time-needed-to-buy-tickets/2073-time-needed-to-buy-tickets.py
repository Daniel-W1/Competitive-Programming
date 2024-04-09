class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        
        while tickets[k]:
            for idx in range(len(tickets)):
                if tickets[idx]:
                    tickets[idx] -= 1
                    ans += 1
                
                if not tickets[k]: break
        
        return ans
            