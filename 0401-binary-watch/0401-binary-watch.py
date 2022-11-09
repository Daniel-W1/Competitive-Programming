class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        times = []
        
        for hour in range(12):
            for minute in range(60):
                current_on = bin(hour).count("1") + bin(minute).count("1")
                if current_on == turnedOn:
                    time = "%d:%02d" % (hour,minute)
                    times.append(time)
        return times