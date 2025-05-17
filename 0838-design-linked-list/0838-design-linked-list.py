class ListNode:
    def __init__(self, value=0, next_node=None):
        self.val = value
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if self.head is None:
            return -1
        
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.val

            count += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode


    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        if self.head is None:
            self.head = newNode
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = newNode


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        newNode = ListNode(val)
        current = self.head
        count = 0

        while current and count < index - 1:
            current = current.next
            count += 1

        if current is None:
            return -1
        
        newNode.next = current.next
        current.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        count = 0

        while current.next and count < index - 1:
            current = current.next 
            count += 1

        if current.next:
            current.next = current.next.next

        return -1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)