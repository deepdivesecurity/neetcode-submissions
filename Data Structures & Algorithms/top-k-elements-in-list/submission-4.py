class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}

        for num in nums: 
            freq_map[num] = freq_map.get(num, 0) + 1

        # Sort values in descending order and grab the first two
        sorted_keys = sorted(freq_map, key=freq_map.get, reverse=True)
        top_k_keys = sorted_keys[:k]
        return top_k_keys