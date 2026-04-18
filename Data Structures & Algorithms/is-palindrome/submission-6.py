class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_string = s[::-1]
        
        for char in [" ", "?",".",",","'", ":"]: 
            s = s.replace(char, "")
            reversed_string = reversed_string.replace(char, "")

        if (s.lower() == reversed_string.lower()): 
            return True
        else: 
            return False