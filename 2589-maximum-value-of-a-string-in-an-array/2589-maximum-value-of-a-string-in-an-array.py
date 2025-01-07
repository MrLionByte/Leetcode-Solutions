class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maximum = 0
        val = 0
        for i in strs:
            if i.isdigit():
                val = int(i)
            else:
                val = len(i)
            if val > maximum:
                maximum = val
        return maximum
