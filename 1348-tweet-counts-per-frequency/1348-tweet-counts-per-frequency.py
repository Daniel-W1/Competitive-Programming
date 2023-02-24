from sortedcontainers import SortedList

class TweetCounts:

    def __init__(self):
        self.records = defaultdict(SortedList)

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.records[tweetName].add(time)
        # print(time, "adding ..")
        
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        
        inc = 86400
        if freq[0] == "m": inc = 60
        elif freq[0] == "h": inc = 3600
            
        cur_range = endTime - startTime + 1
        full_rounds = cur_range // (inc)
        start = self.records[tweetName].bisect_right(startTime-1)
        end = self.records[tweetName].bisect_right(endTime)
        
        ans = []
        cur = min(startTime + inc - 1, endTime)
        prev = start
        
        for _ in range(full_rounds):
            idx = self.records[tweetName].bisect_right(cur)
            ans.append(idx - prev)
            prev = idx
            cur += inc
        
        if cur_range % inc:
            ans.append(end - prev)
        
        return ans