class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        current_average = sum(nums[:k]) / k
        max_average = current_average

        for i in range(k, len(nums)):
            current_average += (nums[i] - nums[i-k]) / k
            if current_average > max_average:
                max_average = current_average
            
        return max_average
