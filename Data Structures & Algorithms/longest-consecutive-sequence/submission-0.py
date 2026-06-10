class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Convert array to set & init variables
        nums_set = set(nums)
        seq = 0
        long_seq = 0

        for num in nums_set: 
            if (num - 1) in nums_set: 
                # Not start of sequence
                print(f"{num} is not the start of a sequence")
            else: 
                # Go through the current sequence until reaching the end
                while num in nums_set: 
                    num += 1
                    seq += 1
                # Check if the current sequence is the longest
                if seq > long_seq: 
                    long_seq = seq
                seq = 0
                
        return long_seq
        