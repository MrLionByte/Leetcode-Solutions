# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp_node = ListNode(0, head)
        prev = temp_node

        while head:
            if head.val != val:
                prev.next = head
                prev = prev.next
            head = head.next
        prev.next = None
        return temp_node.next