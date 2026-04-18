# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        previous = None
        next = None

        # Loop through the linked list until reaching the end
        while current: 
            # Save the next node to be set at the end
            next = current.next
            # Set the current node's link to the previous node
            current.next = previous
            # Set the previous node to the current node
            previous = current
            # Set the current node to the next node
            current = next
        
        return previous
        