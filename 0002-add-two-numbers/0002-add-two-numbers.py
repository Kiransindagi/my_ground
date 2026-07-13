# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Continue looping as long as there are nodes in l1, l2, or a carry leftover
        while l1 or l2 or carry:
            # Get the values from the current nodes, or 0 if the list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the digit part of the total
            current.next = ListNode(total % 10)
            
            # Move our pointers forward
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        # The first node was a dummy, so we return the next node
        return dummy_head.next