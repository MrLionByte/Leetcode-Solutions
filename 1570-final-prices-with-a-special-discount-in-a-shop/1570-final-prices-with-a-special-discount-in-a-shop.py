class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        payable = []
        for i in range(len(prices)):
            payable.append(prices[i])
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    payable[i] = prices[i] - prices[j]
                    break
        return payable