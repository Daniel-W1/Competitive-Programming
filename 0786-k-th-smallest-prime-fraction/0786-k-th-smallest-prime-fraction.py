class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = [(arr[0]/arr[-1], 0, len(arr)-1)]
        visited = set([(0, len(arr)-1)])
        possible_combinations = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while k > 1:
            min_fraction, idx1, idx2 = heappop(heap)
            k -= 1
            
            for dx, dy in possible_combinations:
                new_idxs = (idx1 + dx, idx2 + dy)
                
                if new_idxs[0] >= 0 and new_idxs[1] < len(arr) and new_idxs not in visited:
                    # print(new_idxs)
                    visited.add(new_idxs)
                    heappush(heap, (arr[new_idxs[0]]/arr[new_idxs[1]], new_idxs[0], new_idxs[1]))
                    
        
        return [arr[idx] for idx in heappop(heap)[1:]]