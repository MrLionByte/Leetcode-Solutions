class Solution:
    def isHappy(self, n: int) -> bool:
        checked = set()
        if n == 1:
            return True
        while n not in checked and n != 1:
            answer = 0
            checked.add(n)
            for i in str(n):
                answer += int(i)**2
            if answer == 1:
                return True
            n = answer
        return False