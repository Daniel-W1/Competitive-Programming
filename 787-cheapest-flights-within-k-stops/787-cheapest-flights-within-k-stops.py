class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adjacentMatrix, visited = [[0] * n for _ in range(n)], [-1] * n
        for from_, to, price in flights:
            adjacentMatrix[from_][to] = price
        pq = [[0, src, k+1]]
        while pq:
            currentPrice , currentNode, currentStep = heappop(pq)
            if currentNode == dst: return currentPrice
            if currentStep == 0: continue
            visited[currentNode] = currentStep
            for idx, neighborPrice in enumerate(adjacentMatrix[currentNode]):
                if neighborPrice and currentStep > visited[idx]:
                    heappush(pq, [neighborPrice + currentPrice, idx, currentStep - 1])
        return -1