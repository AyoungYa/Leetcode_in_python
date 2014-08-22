"""
Sort a linked list using insertion sort
"""

__author__ = 'Yang'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        flNode = head.next
        while(flNode):
            seNode = flNode
            indexNode = head
            if indexNode.next.val <= flNode.val:
                indexNode = indexNode.next
            else:
                flNode.next = indexNode.next
                indexNode.next = flNode

            flNode = seNode.next

        return head