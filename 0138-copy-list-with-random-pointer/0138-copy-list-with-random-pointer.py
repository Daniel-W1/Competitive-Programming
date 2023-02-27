"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        '''
            dummy = newhead = Node()
            
            normal traversal 
            
            random 
            next 
            
            we keep a hashmap and add the nodes as a key just like clone graph
        
        '''
        
        node_map = {}
        cur = head
        
        while cur:
            
            # first check if the current node exists
            if cur not in node_map:
                node_map[cur] = Node(cur.val)
            
            the_random = cur.random
            the_next = cur.next
            
            # now create the random and the next if they don't exist
            if the_random and the_random not in node_map:
                node_map[the_random] = Node(the_random.val)
                
            if the_next and the_next not in node_map:
                node_map[the_next] = Node(the_next.val)
            
            
            node_map[cur].random = node_map[the_random] if the_random else None
            node_map[cur].next = node_map[the_next] if the_next else None
            
            cur = cur.next
        
        return node_map[head] if head else None
    