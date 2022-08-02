class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
        
        # bucket sort O(n) time, O(n) space
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]

#         for n in nums:
#             count[n] = 1 + count.get(n, 0)
#         for n, c in count.items():
#             freq[c].append(n)

#         res = []
#         for i in range(len(freq) - 1, 0, -1):
#             for n in freq[i]:
#                 res.append(n)
#             if len(res) == k:
#                 return res

        if k == len(nums): return nums
    
        count = Counter(nums)
        freqs = [(val, key) for key, val in count.items()]
        
        minHeap = []
        
        for pair in freqs:
            if len(minHeap) < k:
                heapq.heappush(minHeap, pair)
            else:
                heapq.heappushpop(minHeap, pair)
        
        return [pair[1] for pair in minHeap]
    
    # time comp O()
