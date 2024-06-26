class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        zero_at_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_at_index], nums[i] = nums[i], nums[zero_at_index]
                zero_at_index += 1