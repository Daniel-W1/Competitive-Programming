class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        cnt = Counter()
        ans = 0
        temp = 2 ** 21
        mod = 10 ** 9 + 7
        
        for val in deliciousness:
            total = temp
            
            while total:
                left = total - val
                ans += cnt[left]
                total //= 2
            
            cnt[val] += 1
        
        return ans % mod