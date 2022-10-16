class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = Counter(s1)
        cnt = {}
        
        if len(s1) > len(s2):
            return False
        
        for idx in range(len(s1)):
            cnt[s2[idx]] = cnt.get(s2[idx], 0) + 1
        
        left = 0
        for idx in range(idx + 1, len(s2)):
            if cnt == cnt1: 
                return True
            
            cnt[s2[idx]] = cnt.get(s2[idx], 0) + 1
            cnt[s2[left]] -= 1
            
            if cnt[s2[left]] == 0:
                del cnt[s2[left]]
            
            left += 1
        
        return cnt == cnt1