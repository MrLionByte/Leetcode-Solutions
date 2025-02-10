class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        length = len(arr)
        inr = 0
        for i in range(length):
            for j in range(i,length+1):
                if len(arr[i:j])%2 != 0:
                    inr += sum(arr[i:j])
                    print("### :",arr[i:j])
        return inr