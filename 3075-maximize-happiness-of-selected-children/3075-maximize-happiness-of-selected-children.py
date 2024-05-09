class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse = True)
        ans = 0

        for idx in range(k):
            ans += max(0, happiness[idx] - idx)
        
        return ans
            
            
        