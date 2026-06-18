class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        # Loop through the list breaking it in half each time until the target is found
        while left <= right:
            # Find the mid point of the list
            mid = (left + right) // 2

            # If the target is the current mid, return it otherwise increment up or down to find the new mid
            if target == nums[mid]: 
                return mid
            elif nums[mid] < target: 
                left = mid + 1
            else: 
                right = mid - 1

        # Return -1 if couldn't find the target
        return -1

            