# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        if not head:
            return None
        while current.next:
            temp = current
            current = temp.next
            temp.next = previous
            previous = temp
        current.next = previous   
        return current

    

