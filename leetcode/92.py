# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if m==n:
            return head
        first = ListNode(1)
        first.next=head
        mark=first
        left=head
        right=head
        for i in range(m-1):
            mark=mark.next
            left=left.next
        for i in range(n-1):
            right=right.next
        s=left.next
        left.next=right.next
        while s != right:
            tmp=s
            s=s.next
            tmp.next=left
            left=tmp
        s.next=left
        mark.next=s
        return first.next

