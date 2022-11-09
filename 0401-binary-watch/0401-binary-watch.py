class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
      
        ans = set()
        def backtrack(cnt, hour, minute):
            if cnt == 0:
                if hour > 11 or minute > 59:
                    return
                hour, minute = map(str, (hour, minute))
                if len(minute) < 2:
                    minute = "0" + minute
                
                res = (hour + ":" + minute)
                if res not in ans: ans.add(res)
                return
            if minute > 59 or hour > 11:
                return
            # choice1 
            for bit in range(4):
                if not hour & (1 << bit):
                    backtrack(cnt - 1, hour|(1<<bit), minute)
            
            # choice2 
            for bit in range(6):
                if not minute & (1 << bit):
                    backtrack(cnt - 1, hour, minute | 1<<bit)
        
        backtrack(turnedOn, 0, 0)
        return list(ans)