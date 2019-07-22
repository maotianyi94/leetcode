#!/usr/bin/env python
#_*_coding:utf-8_*_

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:return head
        length = 0
        node = head
        while(node):
            length += 1
            node = node.next
        k %= length
        if k==0:return head
        node1,node2 = head,head
        while(k>0):
            node2 = node2.next
            k -= 1
        while(node2.next):
            node2 = node2.next
            node1 = node1.next
        newhead = node1.next
        node1.next = None
        node2.next = head
        return newhead