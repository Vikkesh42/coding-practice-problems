#https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode(0)
        dummy=tail

        temp1=list1
        temp2=list2
        while temp1 and temp2 :
            if temp1.val<=temp2.val:
                dummy.next = temp1
             
                temp1=temp1.next
            else:
                dummy.next = temp2
             
                temp2=temp2.next
            dummy=dummy.next

        if temp1:
            dummy.next=temp1
        if temp2:
            dummy.next=temp2
        
        return tail.next
