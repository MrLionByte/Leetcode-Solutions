class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maximum = 0
        for i in strs:
            if i.isdigit():
                if int(i) >= maximum:
                    maximum = int(i)
            else:
                val = len(i)
                if val >= maximum:
                    maximum = val
        return maximum