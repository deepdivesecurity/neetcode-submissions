# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Create a variable for each node that states if it was visited or not
        visited = []
        current = head

        while current: 
            if current in visited: 
                return True
            else: 
                visited.append(current)
            current = current.next
        
        return False
