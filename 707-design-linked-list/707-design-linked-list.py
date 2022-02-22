class ListNode:
    def __init__(self, val = 0, the_next = None) -> None:
        self.val = val
        self.next = the_next
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        the_length = self.length(self.head)
        cur = self.head
        if 0 <= index < the_length:
            while index:
                cur = cur.next
                index -= 1
            return cur.val
        else: return -1 
        

    def addAtHead(self, val: int) -> None:
        new = ListNode(val)
        new.next = self.head
        self.head = new

    def addAtTail(self, val: int) -> None:
        cur = self.head
        if not cur:
            self.head = ListNode(val)
            return
        while cur.next:
            cur = cur.next
        new = ListNode(val)
        cur.next = new
        

    def addAtIndex(self, index: int, val: int) -> None:
        the_length = self.length(self.head)
        cur = self.head
        if 0 <= index <= the_length:
            if index == 0: return self.addAtHead(val)
            elif index == the_length: return self.addAtTail(val)
            else:
                while index-1:
                    cur = cur.next
                    index -= 1
                new, the_next = ListNode(val),cur.next
                cur.next, new.next = new, the_next
        else: return 
        

    def deleteAtIndex(self, index: int) -> None:
        the_length = self.length(self.head)
        cur = self.head
        if 0 <= index < the_length:
            if index == 0: 
                self.head = self.head.next
                return
            while index-1:
                cur = cur.next
                index -= 1
            the_next = cur.next.next
            cur.next = the_next
        else: return
        
    def length(self, head):
        leng = 0
        while head:
            leng += 1
            head = head.next
        return leng
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)