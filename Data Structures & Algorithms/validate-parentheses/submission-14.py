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
                if not stack: 
                    return False
                key = stack.pop()
                if char != brackets[key]: 
                    return False
        
        if len(stack) > 0: 
            return False

        return True

        
