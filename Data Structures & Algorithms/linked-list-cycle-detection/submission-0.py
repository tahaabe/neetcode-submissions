# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prey=head
        hunter=head
        while hunter and hunter.next:
            prey=prey.next
            hunter=hunter.next.next
            if prey==hunter:
                return True
        return False