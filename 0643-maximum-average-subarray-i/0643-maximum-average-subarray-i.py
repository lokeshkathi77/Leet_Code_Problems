from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Compute the sum of the first window
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # Slide the window across the array
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]  # Add next element, remove first element of previous window
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k  # Return the maximum average
