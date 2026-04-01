# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        given head of linked list, return true if theres a cycle
        otherwise return false

        we will have one slow, one fast pointer

        we make the slow one go to next, make the fast one got to next.next

        if there's a cycle, the fast one will eventually be the same as slow

        if no cycle then fast will reach the end (None) first and we can terminate
        """

        if not head: return False
        slow, fast = head, head.next

        while fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next

        return False
