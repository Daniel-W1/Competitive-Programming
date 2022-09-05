class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left, right = 0, 0
        heap = []
        removed = set()
        while k > 1:
            heapq.heappush(heap, (-nums[right], right))
            right += 1
            k -= 1
        
        ans = []
        for idx in range(right, len(nums)):
            heapq.heappush(heap, (-nums[idx], idx))
            while heap[0][1] in removed:
                heapq.heappop(heap)
            ans.append(-heap[0][0])
            removed.add(left)
            left += 1
        return ans
    # time comp O(nlogn)
    # space O(n)
            
            