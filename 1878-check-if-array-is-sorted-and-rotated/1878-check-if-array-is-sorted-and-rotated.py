class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_array = sorted(nums)
       
        for i in range(len(nums)):
            val = nums[i:] + nums[:i]
            if val == sorted_array:
                return True
        return False
