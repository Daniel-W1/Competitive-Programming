class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        ans = 0
        
        left, right = 0, len(tokens)-1
        
        while left <= right:
            ans = max(ans, score)
            if power >= tokens[left]:
                score += 1
                power -= tokens[left]
                left += 1
            elif score >= 1:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break
        
        ans = max(ans, score)
        return ans