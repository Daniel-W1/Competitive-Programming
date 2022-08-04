class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        heap = []
        for i in count:
            heapq.heappush(heap, (-count[i], i))
        output = []
        for i in range(k):
            popped = heapq.heappop(heap)
            output.append(popped[1])
        return output