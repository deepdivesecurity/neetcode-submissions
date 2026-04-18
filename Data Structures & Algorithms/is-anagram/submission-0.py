from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Get the character counts and put into dictionary
        sCount = Counter(s)
        tCount = Counter(t)

        if sCount == tCount: 
            return True
        else: 
            return False


