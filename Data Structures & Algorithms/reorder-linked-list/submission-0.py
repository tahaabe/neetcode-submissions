# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #middle 
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        middle=slow.next
        slow.next=None
        #reverse the middle
        reverse=middle
        prev=None
        while reverse:
            next_node=reverse.next
            reverse.next=prev
            prev=reverse
            reverse=next_node
        #merge
        first=head
        second=prev
        while second:
            tmp1=first.next
            tmp2=second.next

            first.next=second
            second.next=tmp1

            first=tmp1
            second=tmp2
        




        
        