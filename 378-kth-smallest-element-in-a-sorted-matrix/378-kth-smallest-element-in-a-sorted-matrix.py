class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        cnt = 0
        nums = [val for row in matrix for val in row]
        heapq.heapify(nums)
        while k:
            ans = heapq.heappop(nums)
            k -= 1
        return ans
                