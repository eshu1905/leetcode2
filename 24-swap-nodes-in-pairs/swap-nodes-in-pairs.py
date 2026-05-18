# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy

        while prev.next and prev.next.next:
            
            # Nodes to swap
            first = prev.next
            second = prev.next.next

            # Swapping
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev to next pair
            prev = first

        return dummy.next




        
        
        
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        