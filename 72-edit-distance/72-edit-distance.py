class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        mm = len(word1)
        nn = len(word2)
        
        visited = set()
        # (step, left, right)
        queue = [(0, 0, 0)]
        while queue:
            step, left, right = heappop(queue)
            if left == mm and right == nn:
                return step
            if left == mm or right == nn:
                heappush(queue, (step + mm - left + nn - right, mm, nn))
                continue
            if (left,right) in visited:
                continue
            visited.add((left, right))
            if word1[left] == word2[right]:
                heappush(queue, (step, left + 1, right + 1))
                continue
            heappush(queue,(step + 1, left + 1, right + 1))
            heappush(queue,(step + 1, left, right + 1))
            heappush(queue,(step + 1, left + 1, right))