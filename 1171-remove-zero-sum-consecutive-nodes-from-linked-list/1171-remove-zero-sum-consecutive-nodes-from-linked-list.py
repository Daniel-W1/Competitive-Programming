# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            {
                0: -1,
                1: 0,
                3: 1,
                6: 2,
            
            }
                    
        """
        
        def clean_map(value):
            # cleans everything that is after this value
            found = False
            for key in list(node_map.keys()):
                if not found:
                    found = found or key == value
                else:
                    del node_map[key]
            
        
        node_map = {
            0: ListNode()
        }
        node_map[0].next = head
        
        running_sum = 0
        current = head
        
        while current:
            target = current.val
            
            if running_sum + target in node_map:
                node_map[running_sum + target].next = current.next
                clean_map(running_sum + target)
            else:
                node_map[running_sum + target] = current
                
            running_sum += target
            current = current.next
        
        return node_map[0].next
                
                
                
                