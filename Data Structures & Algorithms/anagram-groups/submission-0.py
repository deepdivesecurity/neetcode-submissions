from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        # Loop through the strings from the list
        for s in strs: 
            # Sort the string to create the key (must use tuple because sorted returns a list of chars)
            st = tuple(sorted(s))
            # Add the key to the hash_map and append the original string to a list as the key's value
            hash_map.setdefault(st, []).append(s)

        # Return the hash_map as a list
        return list(hash_map.values())