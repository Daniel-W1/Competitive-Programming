class Solution:
    def minimumBuckets(self, street: str) -> int:
        bucketCount, lastBucketPostion = 0, -1
        length = len(street)
        for i, ch in enumerate(street):
            if ch == 'H':
                if i > 0 and lastBucketPostion == i - 1:
                    continue
                
                if i + 1 < length and street[i + 1] == '.':
                    lastBucketPostion = i + 1
                    bucketCount += 1
                elif i - 1 >= 0 and street[i - 1] == '.':
                    lastBucketPostion = i - 1
                    bucketCount += 1
                else:
                    return -1
        
        return bucketCount