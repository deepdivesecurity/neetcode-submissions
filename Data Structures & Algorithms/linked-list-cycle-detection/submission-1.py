# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        current = head

        # Loop through the list checking if the current node exists in the list
        while current: 
            # If it does exist, it means it has been seen before so return True
            if current in visited: 
                return True
            else: 
                # Otherwise append the current node to the list
                visited.append(current)
            current = current.next
        
        return False
