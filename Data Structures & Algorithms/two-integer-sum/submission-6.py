class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Loop through the list of numbers available
        for i in range(len(nums)): 
            # Loop through again and see if any of the numbers equal the target
            for j in range(len(nums)): 
                # Avoid the same array element
                if i == j: 
                    continue
                # If the numbers equal the target, return their indices
                if nums[i] + nums[j] == target: 
                    return [i, j]
        