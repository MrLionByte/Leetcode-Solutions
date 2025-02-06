class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        L = len(arr)
        count = 0
        for i in range(L-2):
            for j in range(i, L-1):
                temp_i = arr[i] - arr[j]
                if temp_i < 0:
                    temp_i = temp_i*-1
                if temp_i <= a:
                    for k in range(j,L):
                        if i != j and j != k and i != k:
                            temp_j = arr[j] - arr[k]
                            temp_k = arr[i] - arr[k]
                            if temp_j < 0:
                                temp_j = temp_j * -1
                            if temp_k < 0:
                                temp_k = temp_k * -1
                            if temp_j <= b and temp_k <= c:
                                count += 1
        return count