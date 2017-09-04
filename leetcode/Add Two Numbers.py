"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        if not (l1 and l2):
            if l1:
                head.next = l1
            else:
                head.next = l2
        else:
            carry = 0
            p1 = l1
            p2 = l2
            temp = head
            while p1 and p2:
                node = ListNode((p1.val + p2.val + carry) % 10)
                temp.next = node
                temp = temp.next
                carry = (p1.val + p2.val + carry) / 10
                p1 = p1.next
                p2 = p2.next

            while p1:
                node = ListNode((p1.val + carry) %10)
                carry = (p1.val + carry) / 10
                temp.next = node
                temp = temp.next
                p1 = p1.next

            while p2:
                node = ListNode((p2.val + carry) %10)
                carry = (p2.val + carry) / 10
                temp.next = node
                temp = temp.next
                p2 = p2.next
            if carry:
                node = ListNode(carry)
                temp.next = node

        return head.next