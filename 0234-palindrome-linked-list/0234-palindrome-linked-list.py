# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        checker = []
        current = head
        while current:
            checker.append(current.val)
            current = current.next

        return checker == checker[::-1]
