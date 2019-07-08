# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return
        tortoise = head
        hare = head
        # cycle detection
        while hare.next and tortoise.next and hare.next.next:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                # find start node of cycle
                head1 = hare
                head2 = head
                pos = 0
                while head1 != head2:
                    head1 = head1.next
                    head2 = head2.next
                return head2
        return
