class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {"{":"}", "[":"]", "(":")"}
        stack = []

        # Loop through chars of the string
        for char in s: 
            # If the char is an opening bracket, push it to the stack
            if char in brackets: 
                stack.append(char)
            
            # If the char is a closing bracket, check if the last bracket in the stack is the same
            if char in brackets.values(): 
                # First check if the stack has any opening brackets to compare it to, if not return False
                if not stack: 
                    return False
                # Pop the opening bracket from the stack to compare
                key = stack.pop()
                # Check the hashmap if the char is the corresponding closing bracket
                if char != brackets[key]: 
                    return False
        
        # Check if the length of the stack is greater than 0 and return False if so
        if len(stack) > 0: 
            return False

        return True

        
