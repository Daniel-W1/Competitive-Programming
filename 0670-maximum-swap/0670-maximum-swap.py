class Solution:
    def maximumSwap(self, num: int) -> int:
        
        n = str(num)
        ans = num
        
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                
                # print(n[i], n[j],"here")
                new_num = n[:i] + n[j] + n[i+1:j] + n[i] + n[j+1:]
                # print(new_num, n[:i] , n[j+1:])
                ans = max(ans, int(new_num))
        
        return ans
                
                
        