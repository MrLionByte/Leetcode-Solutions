class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        arr = []
        ans = [i for i in range(1,k+1)]
        count = 0
        print("ANS",ans)
        for i in range(len(nums)-1,-1,-1):
            count += 1
            if nums[i] in ans:
                ans.remove(nums[i])
            if len(ans)== 0:
                break
        return count
