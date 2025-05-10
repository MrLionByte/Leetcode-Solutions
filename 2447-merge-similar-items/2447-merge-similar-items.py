class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        count = {}
        
        for val, weight in items1:
            if val in count:
                count[val] += weight
            else:
                count[val] = weight
        
        for val, weight in items2:
            if val in count:
                count[val] += weight
            else:
                count[val] = weight
        
        result = []
        for val in sorted(count.keys()):
            result.append([val,count[val]])

        return result