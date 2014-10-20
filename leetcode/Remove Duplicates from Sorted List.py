"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""
__author__ = 'Yang'

"""
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head){
        if(head){
            ListNode *pp;
            ListNode *p;

            pp = head;
            p = pp->next;
            int temp = pp->val;
            while(p){
                if(temp == p->val){
                    pp->next = p->next;
                    p = p->next;
                }
                else{
                    pp = pp->next;
                    p = p->next;
                    temp = pp->val;
                }
            }
        }
        return head;
    }
};
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head.next:
            pass
        else:
            temp = head.val
            pp = head
            p = head.next
            while p:
                if p.val == temp:
                    pp.next = p.next
                    p = pp.next
                else:
                    pp = pp.next
                    p = p.next
                    temp = pp.val
        return head
