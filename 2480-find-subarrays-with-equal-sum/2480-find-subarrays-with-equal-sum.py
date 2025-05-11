class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        answer = set()
        for i in range(len(nums)-1):
            if nums[i]+nums[i+1] in answer: 
                return True
            answer.add(nums[i]+nums[i+1])
        return False