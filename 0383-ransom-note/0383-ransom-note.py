class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in set(ransomNote):
            if i not in magazine:
                return False
            elif ransomNote.count(i) != magazine.count(i) and ransomNote.count(i) > magazine.count(i):
                return False
        return True
         