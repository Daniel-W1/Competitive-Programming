class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for i, list in enumerate(lists):
            if list:
                heapq.heappush(minHeap, (list.val, i, list))
            
        dummy = tail = ListNode()
        while minHeap:
            _, __, node = heapq.heappop(minHeap)
            next = node.next
            node.next = None
            tail.next = node
            tail = tail.next
            if next:
                heapq.heappush(minHeap, (next.val, __, next))
            
        return dummy.next
        
            