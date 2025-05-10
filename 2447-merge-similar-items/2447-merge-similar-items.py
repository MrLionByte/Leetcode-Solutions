class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        big_array = items1 if len(items1)>len(items2) else items2
        small_array = items2 if big_array == items1 else items1 

        for pair in small_array:
            dummy = None
            for main_pair in big_array:
                if pair[0] == main_pair[0]:
                    main_pair[1] += pair[1]
                    dummy = None
                    break
                if pair[0] != main_pair[0]:
                    dummy = pair
            if dummy:
                big_array.append(dummy)

        return sorted(big_array)
