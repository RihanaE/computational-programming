
class MyLinkedList:

    def __init__(self):
        self.size=0
        self.head=ListNode(0)

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current=self.head
        for i in range(index + 1):
            current=current.next
            
        return current.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

        
    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        self.size +=1
        
        pre=self.head
        for i in range(index):
            pre=pre.next
            
        temp=ListNode(val)
        temp.next=pre.next
        pre.next=temp
        
            
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        self.size -=1
        pre=self.head
        
        for i in range(index):
            pre=pre.next
            
        pre.next=pre.next.next
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)