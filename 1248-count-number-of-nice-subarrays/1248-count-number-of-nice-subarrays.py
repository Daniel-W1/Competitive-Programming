class Solution:
    def numberOfSubarrays(self, arr: List[int], k: int) -> int:
       #[1,1,2,1,1]
       #[1,2,2,3,4]
        
        count = {}
        prefix = []
        prev = 0
        for num in (arr):
            if num%2 != 0:
                prefix.append(prev + 1)
                prev = prefix[-1]
            else: prefix.append(prev)
        for num in prefix:
            c = count.get(num, 0)
            count[num] = c+1
        zero = count.get(0, 0)
        count[0] = zero + 1
        res = 0
        print(prefix)
        for num in prefix:
            if num >= k:
                dif = num - k
                res += count.get(dif, 0)
        return res 