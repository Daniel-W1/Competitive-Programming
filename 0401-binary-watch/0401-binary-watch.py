class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        
        for hour in range(12):
            for minute in range(60):
                current_on = bin(hour).count("1") + bin(minute).count("1")
                if current_on == turnedOn:
                    res = str(hour) + ":" + str(minute) if minute > 9 else str(hour) + ":" + "0"+str(minute)
                    ans.append(res)
        
        return ans