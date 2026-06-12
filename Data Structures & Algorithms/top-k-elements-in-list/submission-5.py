class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        # Go through the list and add the frequency of values to the hashmap
        for num in nums: 
            freq_map[num] = freq_map.get(num, 0) + 1

        # Sort the hashmap and get the top 2 keys
        sorted_keys = sorted(freq_map, key=freq_map.get, reverse=True)
        top_k_keys = sorted_keys[:k]
        
        return top_k_keys