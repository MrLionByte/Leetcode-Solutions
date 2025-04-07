class Solution:
    def sortSentence(self, s: str) -> str:
        string_array = s.split()
        final_answer_array = [""] * len(string_array)
        for word in string_array:
            position = int(word[-1]) -1
            final_answer_array[position] = word[:-1]            
        return " ".join(final_answer_array)

