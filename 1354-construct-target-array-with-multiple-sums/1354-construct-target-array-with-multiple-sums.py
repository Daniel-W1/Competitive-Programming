class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        target = [-val for val in target]
        min_total = len(target)
        heapq.heapify(target)
        while total > min_total:
            popped = -heapq.heappop(target)
            total -= popped
            if popped <= total or total == 0: return False
            res = popped//total
            if popped % total:
                heapq.heappush(target,-(popped-total*res))
                total += popped-total*(res)
            else:
                heapq.heappush(target,-(popped-total*(res-1)))
                total += popped-total*(res-1)
        return total == min_total
        
        