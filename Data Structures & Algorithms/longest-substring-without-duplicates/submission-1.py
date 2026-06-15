class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        length = 0
        L = 0

        for R in range(len(s)): 
            """
            While the right pointer char is in the set thereby indicating a duplicate char
            remove the left pointer char from the set and increment the left pointer by 1
            """
            while s[R] in charSet: 
                charSet.remove(s[L])
                L += 1
            # Add the right pointer char to the set until there is a duplicate
            charSet.add(s[R])
            
            # Get the length of the window with the right pointer - left pointer + 1
            length = max(length, R - L + 1)

        return length

