class Solution:
    def numberOfSubarrays(self, arr: List[int], k: int) -> int:
       #[1,1,2,1,1]
       #[1,2,2,3,4]
        
        count = {0:1}
        prefix = []
        prev = 0
        for num in (arr):
            if num%2 != 0:
                prefix.append(prev + 1)
                prev = prefix[-1]
            else: prefix.append(prev)
        for num in prefix:
            count[num] = count.get(num,0) + 1
        res = 0
        for num in prefix:
            if num >= k:
                dif = num - k
                res += count.get(dif, 0)
        return res 