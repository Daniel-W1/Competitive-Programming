class newElement:
    def __init__(self, word, freq):
        self.content = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return other.content < self.content
        return other.freq > self.freq
    def __eq__(self, other):
        return self.content == other.content and self.freq == other.freq
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        minHeap = []
        count = Counter(words)
        
        for word in count:
            wordobj = newElement(word, count[word])
            if len(minHeap) < k:
                heapq.heappush(minHeap, wordobj)
            else:
                heapq.heappushpop(minHeap, wordobj)
                
        output = []
        while minHeap:
            output.append(heapq.heappop(minHeap).content)
        return output[::-1]
      