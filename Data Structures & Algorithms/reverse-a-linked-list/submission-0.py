# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        given head of linked list, reverse list, returning new beginning of list

        1 -> 2 -> 3 -> 4
        h    n    nn
        h <- t
        1 <- h    t
        need to rearrange pointers so they go opposite

        set temp to head.next, then set temp.next to head, then move head to temp

        """
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev