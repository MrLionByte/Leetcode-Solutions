class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        number_obj = {}
        for n in nums:
            if n in number_obj:
                return n
            else:
                number_obj[n] = 1
        return None