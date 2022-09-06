class TimeMap:

    def __init__(self):
        self.allvalues = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.allvalues[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        array = self.allvalues[key]
        if not array: return ""
        left, right = 0, len(array)-1
        
        while left <= right:
            mid = (left+right)//2
            if array[mid][0] == timestamp:
                return array[mid][1]
            elif array[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1
        
        return array[left-1][1] if array[left-1][0] < timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)