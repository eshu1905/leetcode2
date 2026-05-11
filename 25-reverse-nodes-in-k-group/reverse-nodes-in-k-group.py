# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        def reverse(start,end):
            prev=end
            while start!=end:
                temp=start.next
                start.next=prev
                prev=start
            return prev
        dummy=ListNode(0)
        dummy.next=head
        group=dummy
        while True:
            kth=group
            for _ in range(k):
                kth=kth.next
                if not kth:
                    return dummy.next
            group_next=kth.next
            prev=group_next
            curr=group.next
            while curr!=group_next:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=group.next
            group.next=kth
            group=temp
        return head









        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        