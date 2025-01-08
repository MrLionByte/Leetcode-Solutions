class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        counter = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] == words[j][:len(words[i])] and words[i] == words[j][-len(words[i]):]:
                    counter += 1
        return counter