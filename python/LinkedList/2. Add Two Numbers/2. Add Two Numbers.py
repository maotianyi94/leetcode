#!/usr/bin/env python
#_*_coding:utf-8_*_


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
    python3 
    
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(-1)
        node = head
        tag = 0
        while(l1 and l2):
            add = l1.val + l2.val + tag
            tag = 1 if add >= 10 else 0
            if tag == 1:add -= 10
            node.next = ListNode(add)
            l1 = l1.next
            l2 = l2.next
            node = node.next
        l = l1 if l1  else l2
        while(l):
            add = l.val + tag
            tag = 1 if add >= 10 else 0
            if tag == 1:add -= 10
            node.next = ListNode(add)
            l = l.next
            node = node.next
        if tag == 1:
            node.next = ListNode(1)
        return head.next