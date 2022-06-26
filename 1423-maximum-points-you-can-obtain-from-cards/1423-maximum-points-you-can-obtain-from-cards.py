class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        [1,3,6]
        
        [12,7,1]
        '''
        # we need to remove a subarray of size n-k that has the smallest sum
        preSums = [0] + list(accumulate(cardPoints))
        l,h = 0, len(cardPoints)-k
        minSum = float('inf')
        while h < len(cardPoints)+1:
            minSum = min(minSum, preSums[h]-preSums[l])
            l += 1
            h += 1
        return preSums[-1]-minSum