"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together
the nodes of the first two lists.
"""
__author__ = 'Yang'

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if(not l1):
            return l2
        elif(not l2):
            return l1
        else:
            if l1.val <= l2.val:
                node = l1
                l1 = l1.next
                node.next = None
            else:
                node = l2
                l2 = l2.next
                node.next = None

            temp = node
            while(l1 and l2):
                if l1.val <= l2.val:
                    temp.next = l1
                    l1 = l1.next
                    temp = temp.next
                else:
                    temp.next = l2
                    l2 = l2.next
                    temp = temp.next

            if(l1):
                temp.next = l1
            else:
                temp.next = l2
        return node





