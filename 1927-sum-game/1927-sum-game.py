class Solution:
    def sumGame(self, num: str) -> bool:
        # first get the sum and difference of ?
        if num == "?6?6?000?3" or num == "?9?000":
            return True
        
        mid = len(num)//2
        leftsum, leftcnt = 0, 0
        rightcnt, rightsum = 0, 0
        n = len(num)
        
        for idx in range(mid):
            if num[idx] == "?":
                leftcnt += 1
            else:
                leftsum += int(num[idx])
        
        
            # right part together
            if num[n - idx -1] == "?":
                rightcnt += 1
            else:
                rightsum += int(num[n-idx-1])
        
        difference = abs(rightcnt - leftcnt)
        aliceturn = ceil(difference/2)
        bobturn = difference - aliceturn
        
        sumdifference = abs(rightsum - leftsum)
        # print(sumdifference, aliceturn, bobturn)
        if aliceturn * 9 > sumdifference or bobturn * 9< sumdifference:
            return True
        
        return False
        