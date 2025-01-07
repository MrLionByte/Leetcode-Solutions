class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivot_count = nums.count(pivot)
        left = [i for i in nums if i < pivot]
        right = [i for i in nums if i > pivot]
        return left+pivot_count*[pivot]+right