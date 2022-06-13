class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [[v,k] for k, v in count.items()]
        min_heap = arr[:k]
        heapq.heapify(min_heap)
        for it in arr[k:]:
            heapq.heappushpop(min_heap, it)
        return [p[1] for p in heapq.nsmallest(k, min_heap)]
        
        
            
            
        
                    
            
        


        
        
        

        
            
        
        
