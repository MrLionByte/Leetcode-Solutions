class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            print(11)
            return True
        if len(nums) < 3:
            if sum(nums)%2 == 0:
                print(22)
                return False
            else:
                return True
        for i in range(1,len(nums)-1):
            if (nums[i]+nums[i+1])%2 == 0 or (nums[i]+nums[i-1])%2 == 0 and nums[i]: 
                print(33)
                return False
        return True