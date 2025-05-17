class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        red = nums.count(0)
        white = nums.count(1)
        blue = nums.count(2)

        index = 0
        while index < len(nums):
            if index < red:
                nums[index] = 0
            elif index >= red and index < red+white:
                nums[index] = 1
            else:
                nums[index] = 2
            index += 1
        